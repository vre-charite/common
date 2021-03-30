import unittest
from tests.logger import Logger
from tests.preparetest import SetUpTest

import json


class TestGetEntityId(unittest.TestCase):
    log = Logger(name='test_entity_id.log')
    test = SetUpTest(log)

    @classmethod
    def setUpClass(cls):
        cls.app = cls.test.app
        cls.log = cls.test.log

    @classmethod
    def tearDownClass(cls):
        pass

    def test_01_get_entity_id(self):
        self.log.info("\n")
        self.log.info('01' + 'test get_entity_id'.center(80, '-'))
        params = {'entity_type': 'nfs_file'}
        try:
            res = self.app.get('/v1/utility/id', query_string=params)
            self.log.info(f"RESPONSE STATUS: {res.status_code}")
            self.log.info(f"RESPONSE DATA: {res.data}")
            self.log.info(f"COMPARING: 200 VS {res.status_code}")
            self.assertEqual(res.status_code, 200)
            received_entity_type = json.loads(res.data)['result'].split('-')[0]
            self.log.info(f'COMPARING: {received_entity_type} VS nfs_file')
            self.assertEqual(received_entity_type, params['entity_type'])
        except Exception as e:
            self.log.error(f"GET ERROR: {e}")
            raise e

    def test_02_get_entity_id_without_type(self):
        self.log.info("\n")
        self.log.info('02' + 'test get_entity_id_without_type'.center(80, '-'))
        try:
            res = self.app.get('/v1/utility/id')
            self.log.info(f"RESPONSE STATUS: {res.status_code}")
            res = json.loads(res.data)
            self.log.info(f"RESPONSE RESULT: {res['result']}")
            self.log.info(f"RESPONSE ERROR: {res['error_msg']}")
            self.log.info(f"COMPARING: 200 VS {res['code']}")
            self.assertEqual(res['code'], 200)
        except Exception as e:
            self.log.error(f"GET ERROR: {e}")
            raise e

    def test_03_get_entity_id_int(self):
        self.log.info("\n")
        self.log.info('03' + 'test get_entity_id_int'.center(80, '-'))
        params = {'entity_type': '12345'}
        try:
            res = self.app.get('/v1/utility/id', query_string=params)
            self.log.info(f"RESPONSE STATUS: {res.status_code}")
            self.log.info(f"RESPONSE DATA: {res.data}")
            self.log.info(f"COMPARING: 200 VS {res.status_code}")
            self.assertEqual(res.status_code, 200)
            received_entity_type = json.loads(res.data)['result'].split('-')[0]
            self.log.info(f'COMPARING: {received_entity_type} VS 12345')
            self.assertEqual(received_entity_type, params['entity_type'])
        except Exception as e:
            self.log.error(f"GET ERROR: {e}")
            raise e

    def test_04_get_entity_id_empty_string(self):
        self.log.info("\n")
        self.log.info('04' + 'test get_entity_id_empty_string'.center(80, '-'))
        params = {'entity_type': ''}
        try:
            res = self.app.get('/v1/utility/id', query_string=params)
            self.log.info(f"RESPONSE STATUS: {res.status_code}")
            res = json.loads(res.data)
            self.log.info(f"RESPONSE RESULT: {res['result']}")
            self.log.info(f"RESPONSE ERROR: {res['error_msg']}")
            self.log.info(f"COMPARING: 200 VS {res['code']}")
            self.assertEqual(res['code'], 200)
        except Exception as e:
            self.log.error(f"GET ERROR: {e}")
            raise e


if __name__ == '__main__':
    unittest.main()