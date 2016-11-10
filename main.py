__author__ = 'yura'

from tornado.ioloop import IOLoop
from tornado.web import Application
from routes import routes
from db_config import db_client


def make_app():
    settings = {
        'template_path': 'templates',
        'login_url': '/login',
        'xsrf_cookies': False,
        'debug': True,
        'db': db_client,
        'cookie_secret': 'jJPkVXv8SiW850psVdvGU0lhAIrmPEN/rHDGAvBW8tY='
    }
    return Application(routes, **settings)


def main():
    app = make_app()
    app.listen(8888)
    io_loop = IOLoop.instance()
    io_loop.start()

if __name__ == "__main__":
    main()

