import requests
from common.services.logger_services.logger_factory_service import SrvLoggerFactory
from common.config import ConfigClass
from common.models.config_center_policy import ConfigCenterPolicy
from common.vault.vault_exception import VaultClientException, VaultClientError

class VaultClient():
    _logger = SrvLoggerFactory('vault_client').get_logger()

    def __init__(self, vault_service: str, vault_crt: str, vault_token: str):
        self.vault_service = vault_service
        self.vault_crt = vault_crt
        self.vault_headers = { "X-Vault-Token": vault_token }

    """Get config based on service namespace"""
    def get_from_vault(self, srv_namespace: str) -> dict:
        try:
            # fetch Vault stored configurations
            self._logger.info(f"Fetching configs from Vault")
            vault_gotten = requests.get(
                self.vault_service,
                verify = self.vault_crt,
                headers = self.vault_headers
            )
            if vault_gotten.status_code != 200:
                self._logger.info(vault_gotten.text)
                raise VaultClientException(VaultClientError.CONNECT_ERROR)

            # check Vault response
            vault_gotten_json = vault_gotten.json()
            if 'data' not in vault_gotten_json:
                self._logger.info(vault_gotten.text)
                raise VaultClientException(VaultClientError.RESPONSE_ERROR)

            # -grant access to service "srv_namespace"
            # default return all configurations-
            # since we might use the vault to directly
            # handle the service return. for now I will just return ALL
            vault_data: dict = vault_gotten_json['data']
            # granted = ConfigCenterPolicy.get_granted(srv_namespace)
            # config_return = {}
            # for k, v in vault_data.items():
            #     validate = lambda key, section: section in key
            #     is_granted = any([validate(k, section) for section in granted])
            #     if is_granted:
            #         config_return[k] = v
            # return config_return if granted else vault_data
            return vault_data

        except Exception as e:
            self._logger.error(f"Exception: {e}")
