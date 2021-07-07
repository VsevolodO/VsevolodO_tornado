import tornado.ioloop
import tornado.web
import tornado.websocket


port = 9000
information = {
    "user": "Test",
    "port": port   
}


class EchowebSocket(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        print('opened WS')

    def on_message(self, data):
        if data == 'hello':
            self.write_message(information)
        else:
            self.write_message("wrong!")
        


    def on_close(self):
        print('WS closed') 



def make_app():
    return tornado.web.Application([
        (r"/" ,EchowebSocket)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(port)
    print("server started")
    tornado.ioloop.IOLoop.current().start()
    