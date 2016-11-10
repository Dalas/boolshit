from tornado import gen
from controller.page import BasePageHandler
import json
import bcrypt
import concurrent.futures
import tornado.escape
from tornado import gen
from models import User
from tornado.web import HTTPError
import datetime
import uuid
from models import Session

executor = concurrent.futures.ThreadPoolExecutor(2)


class RegisterPageHandler(BasePageHandler):
    @gen.coroutine
    def get(self):
        self.render('register.html', user_data={'first_name': '', 'email': '', 'last_name': ''}, error={})

    @gen.coroutine
    def post(self):
        email = self.get_argument('email', default='')
        first_name = self.get_argument('first_name', default='')
        last_name = self.get_argument('last_name', default='')
        password1 = self.get_argument('password1', default='')
        password2 = self.get_argument('password2', default='')

        same_email_user = yield self.settings['db'].User.find_one({'email': email})

        if same_email_user:
            self.render('register.html', error='User with this email already exist.',
                        user_data={'first_name': first_name, 'email': email, 'last_name': last_name})
            return

        if password1 != password2:
            self.render('register.html', error='Passwords doesn\'t match',
                        user_data={'first_name': '', 'email': '', 'last_name': ''})
            return
        # if self.check_password(password1):
        #     self.render('register.html', error='Incorrect Password',
        #                 user_data={'first_name': '', 'email': '', 'last_name': ''})

        hashed_password = yield executor.submit(
            bcrypt.hashpw, tornado.escape.utf8(password1),
            bcrypt.gensalt())

        user_dict = {'first_name': first_name, 'email': email, 'last_name': last_name,
                     'password': hashed_password,
                     'permission': 'admin', 'group': ''}

        user_id = yield User.create_fulled(user_dict)
        session = yield Session.create(user_id)

        self.set_secure_cookie('token', session['token'])
        self.redirect('/')
