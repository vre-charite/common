# Copyright 2022 Indoc Research
# 
# Licensed under the EUPL, Version 1.2 or – as soon they
# will be approved by the European Commission - subsequent
# versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the
# Licence.
# You may obtain a copy of the Licence at:
# 
# https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
# 
# Unless required by applicable law or agreed to in
# writing, software distributed under the Licence is
# distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.
# See the Licence for the specific language governing
# permissions and limitations under the Licence.
# 

import os

import pytest
from dotenv import load_dotenv
from pytest_httpx import HTTPXMock

from common.vault.vault_client import VaultClient
from common.vault.vault_exception import VaultClientException


class TestVaultClient:
    mock_service = 'https://mock_url'
    mock_crt = ''
    mock_token = 'mock_token'
    client = VaultClient(mock_service, mock_crt, mock_token)

    def test_01_get_from_vault_service_notification(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(url=self.mock_service, json={'data': {'secret_1': 'value_1'}})
        secrets = self.client.get_from_vault('service_notification')
        assert type(secrets) == dict
        assert len(secrets) > 0

    def test_02_get_from_vault_service_kg(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(url=self.mock_service, json={'data': {'secret_1': 'value_1'}})
        secrets = self.client.get_from_vault('service_kg')
        assert type(secrets) == dict
        assert len(secrets) > 0

    def test_03_get_from_vault_connect_error(self):
        with pytest.raises(VaultClientException, match='Failed to connect to Vault'):
            invalid_client = VaultClient(
                'https://vault.com/invalid-url', '', 'mock_token'
            )
            invalid_client.get_from_vault('service_notification')

    def test_04_get_from_vault_response_error(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(url=self.mock_service, json=['invalid'])
        with pytest.raises(VaultClientException, match='Received invalid response from Vault'):
            self.client.get_from_vault('service_notification')
