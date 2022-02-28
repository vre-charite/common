import requests
import time
from common.app import create_app

class SetUpTest:

    def __init__(self, log):
        self.log = log
        self.app = self.create_test_client()

    def create_test_client(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        test_client = app.test_client(self)
        return test_client