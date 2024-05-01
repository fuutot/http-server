from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Sample web-server')
        return

server = HTTPServer(("", 8000), HelloServerHandler)
server.serve_forever()