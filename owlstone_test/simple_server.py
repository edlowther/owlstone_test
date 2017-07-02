from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    """Serves files from the project as requested by the network."""
    def do_GET(self):
        path = './owlstone_test' + self.path
        if self.path == '/':
            path += 'index.html'
        with open(path, 'rb') as f:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f.read())

def run(server_class=HTTPServer, handler_class=Handler):
    """Runs the server on port 8000 using the associated custom Handler class."""
    PORT = 8000
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    try:
        print('Serving forever on port {}...'.format(PORT))
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Ending session...')