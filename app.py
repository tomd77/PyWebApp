import json


def application(environ, start_response):

    # will be returned to the client
    server_response = {'success': False,
                       'return_code': 1,
                       'info_message': ""
                      }

    # Find out how many bytes are in the request body
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    # When the method is POST we expect that data is passed from client to server.
    # The data is stored in wsgi.input variable.
    request_type = environ.get('REQUEST_METHOD')

    if request_type == 'POST':
        request_body = environ['wsgi.input'].read(request_body_size)
        data = json.loads(request_body)
        server_response['info_message'] += f"Server received {request_type} request "
        server_response['info_message'] += f"with data: {data}. "
        server_response['success'] = True
        server_response['return_code'] = 0

    else:
        server_response['info_message'] += f"Sorry, Server only handles POST requestS"

    # Send WSGI that Python app received back to client.
    # Just to give an idea of what is actually passed to the Python app
    request_environ = []
    for key, value in sorted(environ.items()):
        request_environ.append( '%s: %s' % (key, value))
    server_response['environ_client'] = request_environ  

    # Create json object of the server_response dict
    server_response_json = json.dumps(server_response)
    server_response_bytes = bytes(server_response_json, encoding= 'utf-8')

    # Send response to client
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(server_response_bytes)))
    ]
    start_response(status, response_headers)

    return [server_response_bytes]
