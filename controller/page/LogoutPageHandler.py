from tornado import gen
from controller.page import BasePageHandler
from models import Session


class LogoutPageHandler(BasePageHandler):

    @gen.coroutine
    def get(self):
        token = self.get_secure_cookie('token')
        if token:
            yield Session.delete_session_by_token(token)
        self.clear_cookie(name='token')
        self.redirect('/')
