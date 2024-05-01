from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

with open('index.html', mode='r') as f:
    index = f.read()
with open('next.html', mode='r') as f:
    next = f.read()

routes = []
def route(path, method):
    routes.append((path, method))

route('/', 'index')
route('/index', 'index')
route('/next', 'next')

# BaseHTTPRequestHandlerを継承して独自のRequestHandlerを作る
class HelloServerHandler(BaseHTTPRequestHandler):

    # ルーティング
    def do_GET(self):
        global routes
        _url = urlparse(self.path) # path: アクセスされたパスを保管するプロパティ
        for r in routes:
            if (r[0] == _url.path):
                eval('self.' + r[1] + '()') # evalで評価
                break
        else:
            self.error()
        return
    
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
        _url = urlparse(self.path)
        query = parse_qs(_url.query)
        id = query['id'][0]
        password = query['pass'][0]
        msg = f'id={id}, password={password}'
        self.send_response(200)
        self.end_headers()
        html = next.format(
            title = 'Hi again',
            message = msg,
            data = query
        )
        self.wfile.write(html.encode('utf-8'))
        return

    def error(self):
        self.send_error(404, "CANNOT ACCESS!!")
        return

server = HTTPServer(("", 8000), HelloServerHandler)
server.serve_forever()