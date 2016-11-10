__author__ = 'yura'

from db_config import db_client
import uuid
import binascii, os
from tornado import gen
from datetime import datetime


class Session:
    @classmethod
    @gen.coroutine
    def create(cls, user_id):
        access_token = binascii.b2a_base64(os.urandom(64)).decode('ascii').rstrip('\n')
        session = {'_id': str(uuid.uuid4()), 'token': access_token, 'created': datetime.now(), 'user_id': user_id}
        result_id = yield db_client.Session.insert(session)
        session = yield db_client.Session.find_one({'_id': result_id})
        return session

    @classmethod
    @gen.coroutine
    def get(cls, user_id):
        session = yield db_client.Session.find_one({'_id': user_id})
        return session

    @classmethod
    @gen.coroutine
    def delete_session_by_token(cls, token):
        result = yield db_client.Session.remove({'token': str(token)})
        return result
