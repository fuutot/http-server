from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer

with open('index.html', mode='r') as f:
    index = f.read()
with open('next.html', mode='r') as f:
    next = f.read()

# BaseHTTPRequestHandlerを継承して独自のRequestHandlerを作る
class HelloServerHandler(BaseHTTPRequestHandler):

    # ルーティング
    def do_GET(self):
        _url = urlparse(self.path)
        if (_url.path == '/'):
            self.index()
        elif (_url.path == '/next'):
            self.next()
        else:
            self.error()

    def index(self):
        self.send_response(200)
        self.end_headers()
        html = index.format(
            title = 'Hello from python',
            message = 'Welcom to python'
        )
        self.wfile.write(html.encode('utf-8'))
        return
    
    def next(self):
        self.send_response(200)
        self.end_headers()
        html = next.format(
            title = 'Hi again',
            message = 'This is next page'
        )
        self.wfile.write(html.encode('utf-8'))
        return

    def error(self):
        self.send_error(404, "CANNOT ACCESS!!")
        return

server = HTTPServer(("", 8000), HelloServerHandler)
server.serve_forever()