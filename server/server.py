import socketserver
from http.server import HTTPServer, SimpleHTTPRequestHandler

class Server(SimpleHTTPRequestHandler):
    PORT = 8000

    def do_GET(self):

        pass

    @staticmethod
    def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
        server_address = ('', Server.PORT)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()


with socketserver.TCPServer(("", Server.PORT), Server) as httpd:
    print("serving at port", Server.PORT)
    httpd.serve_forever()