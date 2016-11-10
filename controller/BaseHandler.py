from tornado.web import RequestHandler
from models import User
from tornado import gen
from tornado.escape import json_encode
from tornado.web import HTTPError
import json
import traceback


class BaseHandler(RequestHandler):

    @gen.coroutine
    def prepare(self):
        token = self.get_secure_cookie('token')
        db = self.settings['db']

        if token:
            token = token.decode('utf-8')
        else:
            self.user = None
            return

        session = yield db.Session.find_one({'token': token})
        if not session:
            self.user = None
        else:
            self.user = yield User.get(session['user_id'])


"""
    def write_json_error(self, status_code, **kwargs):
        self.set_header('Content-Type', 'text/json')
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            lines = []
            for line in traceback.format_exception(*kwargs["exc_info"]):
                lines.append(line)
            self.finish(json.dumps({
                'error': self._reason,
                'code': status_code,
                'traceback': lines,

            }))
        else:
            self.finish(json.dumps({
                'error': self._reason,
                'code': status_code,
            }))

    def render_json(self, status_code, reason, data={}):
        self.set_header("Content-Type", "application/json")
        self.set_status(status_code, reason)
        self.write(data)


def auth(handler):
    @gen.coroutine
    def check_token(self, *args, **kwargs):
        db = self.settings['db']
        self.token = self.request.headers.get('token')
        if not self.token:
            self.token = self.get_secure_cookie('token')

            if self.token:
                self.token = self.token.decode('utf-8')
            else:
                raise HTTPError(403, "Forbidden, access denied.", reason="Forbidden, access denied.")

        user_bson = yield db.User.find_one({'sessions': self.token})
        if not user_bson:
            raise HTTPError(401, "Session not found", reason="Session not found")
        else:
            self.user = User.from_son(user_bson)
            return handler(self, *args, **kwargs)

    return check_token


def api_auth(handler):
    @gen.coroutine
    def check_token(self, *args, **kwargs):
        self.token = self.request.headers['token']
        db = self.settings['db']
        user_bson = yield db.User.find_one({'sessions': self.token})
        if not user_bson:
            self.set_status(401, 'Token not found')
            self.set_header("Content-Type", "application/json")
            self.write(json_encode({"error": "Token not found"}))
        else:
            self.user = User.from_son(user_bson)
            return handler(self, *args, **kwargs)

    return check_token


def web_auth(handler):
    @gen.coroutine
    def check_token(self, *args, **kwargs):
        db = self.settings['db']
        token = self.get_secure_cookie('token')
        if token:
            token = token.decode('utf-8')
        user_bson = yield db.User.find_one({'sessions': token})
        if not user_bson:
            self.redirect('/login')
            return
        else:
            self.user = User.from_son(user_bson)
            self.token = token
            return handler(self, *args, **kwargs)

    return check_token
"""