from controller.page import BasePageHandler
from tornado import gen
from tornado.web import asynchronous


class FileUploadingHandler(BasePageHandler):
    @asynchronous
    @gen.coroutine
    def get(self):
        self.render('upload-my-project.html', user=self.user)
