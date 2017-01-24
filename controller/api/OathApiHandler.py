from tornado import gen
from oauth2client.client import flow_from_clientsecrets
from models import User, Session
import httplib2
import json
from controller.api import BaseAPIHandler
from models import User
from collections import defaultdict


class OathApiHandler(BaseAPIHandler):
    @gen.coroutine
    def get(self):
        flow = flow_from_clientsecrets('credentials/client_secrets.json',
                                       scope='https://www.googleapis.com/auth/userinfo.email',
                                       redirect_uri='http://course-project.kh.ua:8888/login')
        if 'code' not in self.request.arguments.keys():
            url = flow.step1_get_authorize_url()
            self.redirect(url)
        else:
            code = self.get_argument('code')
            credentials = flow.step2_exchange(code)
            http_auth = credentials.authorize(httplib2.Http())
            me = http_auth.request('https://www.googleapis.com/oauth2/v1/userinfo?alt=json')
            user_google_dict = json.loads(me[1].decode('utf-8'))

            user = yield User.get_one_by('email', user_google_dict['email'])
            if user:
                session = yield Session.create(user['_id'])
            elif '@nure' not in user_google_dict['email']:
                self.render('error-auth.html', error='Incorrect email address: {0}'.format(user_google_dict['email']),
                            user=None)
                return
            else:
                user_def = defaultdict(lambda: '', user_google_dict)
                result_id = yield User.create_from_google_json(user_def)
                session = yield Session.create(result_id)

            self.set_secure_cookie('token', session['token'])

            self.redirect('/')
