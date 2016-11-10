__author__ = 'yura'

from tornado.web import url
from tornado.web import StaticFileHandler
from controller import *

routes = [
    # Static files.
    url(r'/static/(.*)', StaticFileHandler, {'path': 'static'}),

    # web
    url(r'/', HomePageHandler, name='home'),
    url(r'/login', OathApiHandler, name='login'),
    url(r'/sign_in', LoginPageHandler, name='sign_in'),
    url(r'/sign_up', RegisterPageHandler, name='sign_up'),
    url(r'/sign_out', LogoutPageHandler, name='sign_out'),
    url(r'/account', AccountInfoHandler, name='account'),
    url(r'/google', GoogleExampleHandler, name='google'),
    url(r'/upload_project', FileUploadingHandler, name='upload_project'),

    # web admin
    url(r'/users_list', AdminUsersPageHandler, name='users_list'),

    # api

    # admin
    url(r'/admin/users', AdminUsersPageHandler, name='users_table'),




    #import
    url(r'/import/users', ImportUsers)
]
