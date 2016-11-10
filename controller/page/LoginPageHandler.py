from tornado import gen
from controller.page import BasePageHandler
import bcrypt
import concurrent.futures
import tornado.escape
from models import User, Session

executor = concurrent.futures.ThreadPoolExecutor(2)


class LoginPageHandler(BasePageHandler):
    @gen.coroutine
    def get(self):
        self.render('login.html', error={}, user_email={})

    @gen.coroutine
    def post(self):
        email = self.get_argument('email', default='')
        password = self.get_argument('password', default='')
        user = yield self.settings['db'].User.find_one({'email': email})

        if not user:
            self.render('login.html', user_email=email, error='User with this email does not exist')

        hashed_password = yield executor.submit(
            bcrypt.hashpw, tornado.escape.utf8(password),
            user['password'])

        if user['password'] == hashed_password:
            session = yield Session.create(user['_id'])
            self.set_secure_cookie('token', session['token'])
            self.redirect('/')
        else:
            self.render('login.html', user_email=email, error='Incorrect password')
