import tornado.web
import tornado.ioloop


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World this is a python web server in the backend")


class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./animals.html")


class queryParamterRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if (num.isdigit()):
            r = "odd" if int(num) % 2 else "even"
            self.write(f"{num} is {r}")
        else:
            self.write(f"{num} is not a valid integer")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/animals", listRequestHandler),
        (r"/isEven", queryParamterRequestHandler)
    ])

    port = 8882
    app.listen(port)
    print(f"Applicaiton is listening on port: {port}")
    tornado.ioloop.IOLoop.current().start()
