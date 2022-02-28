import unittest
from tests.logger import Logger
from common.geid.geid_client import GEIDClient


class TestGEIDClient(unittest.TestCase):
    log = Logger(name='test_geid_client.log')

    def test_01_get_GEID(self):
        self.log.info("\nTest case 1: Get GEID")
        client = GEIDClient()
        geid = client.get_GEID()
        self.log.info(f"GEID: {geid}")
        self.assertIsInstance(geid, str)
        self.assertEqual(len(geid), 47)

    def test_02_get_bulk_GEID(self):
        self.log.info("\nTest case 2: Get 5 GEIDs")
        client = GEIDClient()
        geids = client.get_GEID_bulk(5)
        self.log.info(f"GEIDs: {geids}")
        self.assertIsInstance(geids, list)
        self.assertEqual(len(geids), 5)
