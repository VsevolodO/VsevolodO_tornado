import tornado.ioloop
import tornado.web


port = 7000
information = {
    "user": "Test",
    "port": port   
}





class MainHandler(tornado.web.RequestHandler):
     def get(self):
         self.write(information)
         print('get')

def make_app():
    return tornado.web.Application([
        (r"/" ,MainHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(port)
    print("server started")
    tornado.ioloop.IOLoop.current().start()
    