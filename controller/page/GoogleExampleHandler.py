from tornado import gen
from controller.page import BasePageHandler, web_auth
from tornado.web import asynchronous


class GoogleExampleHandler(BasePageHandler):
    @web_auth
    @asynchronous
    @gen.coroutine
    def get(self):
        self.render('google_example.html', user=self.user)
