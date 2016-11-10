from controller import BaseHandler
from tornado import gen
from models import User
from controller.scripts.import_csv import import_data


class BasePageHandler(BaseHandler):
    pass


def web_auth(handler):
    @gen.coroutine
    def check_token(self, *args, **kwargs):
        db = self.settings['db']
        token = self.get_secure_cookie('token')
        if token:
            token = token.decode('utf-8')
        session = yield db.Session.find_one({'token': token})
        if not session:
            return self.redirect('/')
        else:
            self.user = yield User.get(session['user_id'])
            self.token = token
            return handler(self, *args, **kwargs)

    return check_token


def admin_auth(handler):
    @gen.coroutine
    def check_token(self, *args, **kwargs):
        if self.user['permission'] == 'admin':
            return handler(self, *args, **kwargs)
        else:
            return self.redirect('/')

    return check_token


class ImportUsers(BasePageHandler):
    def get(self):
        users = import_data()

        for user in users:
            User.create_fulled(user)

        self.write('asd')
