import socketserver


class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('SocketServer————Got connection from ', addr)
        self.wfile.write('Thank you for connecting'.encode())


server = socketserver.TCPServer(('', 1234), Handler)
server.serve_forever()
