from controller.page import BasePageHandler, web_auth, admin_auth
from tornado import gen
from tornado.web import asynchronous


class AdminUsersPageHandler(BasePageHandler):

    @gen.coroutine
    def get(self):
        self.render('AdminUsersTable.html', user=self.user)
