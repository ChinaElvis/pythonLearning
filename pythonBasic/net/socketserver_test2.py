import socketserver


class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class Handler(socketserver.StreamRequestHandler):
    def handler(self):
        addr = self.request.getpeername()
        print('SocketServer Thread——got connection from ', addr)
        self.wfile.write('Thank you for connecting'.encode())


server = Server(('', 1234), Handler)
server.serve_forever()
