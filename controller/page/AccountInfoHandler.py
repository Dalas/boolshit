from tornado import gen
from controller.page import BasePageHandler, web_auth
from tornado.web import asynchronous

class AccountInfoHandler(BasePageHandler):

    @web_auth
    @asynchronous
    @gen.coroutine
    def get(self):
        self.render('AccountInfo.html', user=self.user)
