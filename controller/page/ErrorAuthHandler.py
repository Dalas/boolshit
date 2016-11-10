from controller.page import BasePageHandler
from tornado import gen
from tornado.web import asynchronous


class ErrorAuthHandler(BasePageHandler):

    @asynchronous
    @gen.coroutine
    def get(self):
        self.render('error-auth.html')
