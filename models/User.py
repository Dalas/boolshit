__author__ = 'yura'

from db_config import db_client
from tornado import gen
import uuid
import binascii
import os


class User:
    @classmethod
    @gen.coroutine
    def create(cls, user_dict):
        user_dict['_id'] = str(uuid.uuid4())
        result_id = yield db_client.User.insert(user_dict)
        return result_id

    @classmethod
    @gen.coroutine
    def create_from_google_json(cls, user_google_dict):
        if not user_google_dict['picture']:
            user_google_dict[
                'picture'] = 'https://lh3.googleusercontent.com/-XdUIqdMkCWA/AAAAAAAAAAI/AAAAAAAAAAA/4252rscbv5M/photo.jpg'

        user_dict = {'_id': str(uuid.uuid4()), 'gender': user_google_dict['gender'], 'permission': 'student',
                     'google_link': user_google_dict['link'], 'first_name': user_google_dict['given_name'],
                     'last_name': user_google_dict['family_name'], 'image_url': user_google_dict['picture'],
                     'email': user_google_dict['email'], 'password': '', 'group': '', 'email_verified': False}

        result_id = yield db_client.User.insert(user_dict)
        return result_id

    @classmethod
    @gen.coroutine
    def get(cls, user_id):
        user = yield db_client.User.find_one({'_id': user_id})
        return user

    @classmethod
    @gen.coroutine
    def get_one_by(cls, name, value):
        user = yield db_client.User.find_one({name: value})
        return user

    @classmethod
    @gen.coroutine
    def create_fulled(cls, user_dict):
        user_id = str(uuid.uuid4())
        fulled_dict = {'_id': user_id, 'gender': '', 'email_verified': False,
                       'permission': user_dict['permission'], 'google_link': '', 'first_name': user_dict['first_name'],
                       'last_name': user_dict['last_name'],
                       'image_url': 'https://lh3.googleusercontent.com/-XdUIqdMkCWA/AAAAAAAAAAI/AAAAAAAAAAA/4252rscbv5M/photo.jpg',
                       'email': user_dict['email'], 'password': user_dict['password'], 'group': user_dict['group']}

        result = yield db_client.User.insert(fulled_dict)
        return user_id
