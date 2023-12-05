import tornado.web
import tornado.ioloop
import json


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


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


class resourceParameterRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseId):
        self.write(
            f"Welcome {studentName} the course you are viewing is {courseId}")


class fruitHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("fruit.txt", "r")
        fruits = fh.read().splitlines()
        fh.close()

        self.write(json.dumps(fruits))

    def post(self):
        fruit = self.get_argument("fruit")
        fh = open("fruit.txt", "a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added successfully."}))


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/animals", listRequestHandler),
        (r"/isEven", queryParamterRequestHandler),
        (r"/students/([a-z]+)/([0-9]+)", resourceParameterRequestHandler),
        (r"/fruits", fruitHandler),
    ])

    port = 8882
    app.listen(port)
    print(f"Applicaiton is listening on port: {port}")
    tornado.ioloop.IOLoop.current().start()
