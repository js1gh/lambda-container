import tornado.ioloop
import tornado.web
from tornado.web import URLSpec as url_spec

class Counter(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self):
        message = f"Counter value is {self.db['counter']}."
        print(message)
        self.write({"counter": self.db['counter']})

    def post(self):
        old_counter_value = self.db['counter']
        self.db['counter'] = old_counter_value + 1
        message = f"Counter value has been updated from {old_counter_value} to {self.db['counter']}."
        print(message)
        self.write({"counter": self.db['counter']})

    def delete(self):
        self.db['counter'] = 0
        message = f"Counter value has been reset to 0."
        print(message)
        self.write({"counter": 0})

def make_app():
    db = {"counter": 0}
    return tornado.web.Application([
        url_spec(r"/counter", Counter, dict(db=db)),
    ])

if __name__ == "__main__":
    app = make_app()
    port_to_listen_on = 8081
    app.listen(port_to_listen_on)
    print(f"The app is now running at localhost:{port_to_listen_on}")
    tornado.ioloop.IOLoop.current().start()

