from controller.page import BasePageHandler
from controller.page import web_auth
from tornado import gen
from tornado.web import asynchronous


class HomePageHandler(BasePageHandler):

    @asynchronous
    @gen.coroutine
    def get(self):
        user = self.user if hasattr(self, 'user') else None

        self.render('home.html', user=user)
