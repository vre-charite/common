import unittest
import os
from tests.logger import Logger
from common.vault.vault_client import VaultClient
from dotenv import load_dotenv


class TestVaultClient(unittest.TestCase):
    log = Logger(name='test_vault_client.log')

    def test_01_get_from_vault_service_notification(self):
        load_dotenv('tests/.env')
        self.log.info("\nTest case 1: Get from Vault for service_notification")
        client = VaultClient(os.getenv('VAULT_URL'), os.getenv('VAULT_CRT'), os.getenv('VAULT_TOKEN'))
        secrets = client.get_from_vault('service_notification')
        self.log.info(f"Vault secrets: {secrets}")
        self.assertIsInstance(secrets, dict)
