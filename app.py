from http.server import BaseHTTPRequestHandler, HTTPServer

with open('index.html', mode='r') as f:
    index = f.read()

# BaseHTTPRequestHandlerを継承して独自のRequestHandlerを作る
class HelloServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(index.encode('utf-8'))
        return

server = HTTPServer(("", 8000), HelloServerHandler)
server.serve_forever()