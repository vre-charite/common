from flask_restx import Resource, fields
from flask import request
from common.services.logger_services.logger_factory_service import SrvLoggerFactory
from common.api_response import APIResponse, EAPIResponseCode
from common.api.namespace import api_service_utility
from common.models.config_center_policy import ConfigCenterPolicy
import requests
from common.config import ConfigClass

get_return = """
            {
                "code": 200,
                "error_msg": "",
                "result": {
                    "ENV": "dev",
                    "NEO4J_SERVICE": "http://10.3.7.216:5062",
                    "DATA_OPS_GR": "http://10.3.7.234:5063",
                    "PROVENANCE_SERVICE": "http://10.3.7.202:5077",
                    "QUEUE_SERVICE": "http://10.3.7.214:6060",
                    "UTILITY_SERVICE": "http://10.3.7.222:5062",
                    "KEYCLOAK_URL": "http://10.3.7.220",
                    "MINIO_OPENID_CLIENT": "react-app",
                    "MINIO_ENDPOINT": "10.3.7.220",
                    "MINIO_HTTPS": False,
                    "MINIO_TEST_PASS": "admin",
                    "REDIS_HOST": "10.3.7.233",
                    "REDIS_PORT": 6379,
                    "REDIS_DB": 0,
                    "REDIS_PASSWORD": "5wCCMMC1Lk",
                    "DOWNLOAD_SRV_KEY": "indoc101",
                    "DOWNLOAD_TOKEN_EXPAT": 5
                }
            }
            """

class APIConfigCenter(Resource):
    _logger = SrvLoggerFactory('api_config_center').get_logger()

    @api_service_utility.response(200, get_return)
    def get(self, srv_namespace):
        """Get config based on service namespace"""
        api_response = APIResponse()
        try:
            # fetch vault stored configurations
            self._logger.info(f"Fetching configs from vault")
            vault_headers = {
                "X-Vault-Token": ConfigClass.VAULT_TOKEN
            }
            vault_gotten = requests.get(
                ConfigClass.VAULT_SERVICE,
                verify=ConfigClass.VAULT_CRT,
                headers=vault_headers)
            if vault_gotten.status_code != 200:
                self._logger.info(vault_gotten.text)
                api_response.set_code(EAPIResponseCode.internal_error)
                api_response.set_result(vault_gotten.text)
                api_response.set_error_msg("Fatal! Vault service connection error.")
                return api_response.to_dict, api_response.code
            api_response.set_code(EAPIResponseCode.success)

            # check vault response
            vault_gotten_json = vault_gotten.json()
            if 'data' not in vault_gotten_json:
                self._logger.info(vault_gotten.text)
                api_response.set_code(EAPIResponseCode.internal_error)
                api_response.set_result(vault_gotten.text)
                api_response.set_error_msg("Fatal! Vault service API error.")
                return api_response.to_dict, api_response.code

            # Grant access to Service: "srv_namespace"
            # default return all configurations
            vault_data: dict = vault_gotten_json['data']
            granted = ConfigCenterPolicy.get_granted(srv_namespace)
            config_return = {}
            for k, v in vault_data.items():
                validate = lambda key, section: section in key
                is_granted = any([validate(k, section) for section in granted])
                if is_granted:
                    config_return[k] = v
            api_response.set_result(config_return if granted else vault_data)
            return api_response.to_dict, api_response.code
        except Exception as e:
            self._logger.error(f"ERROR HAPPENED: {e}")
            api_response.set_code(EAPIResponseCode.internal_error)
            api_response.set_result(e)
            return api_response.to_dict, api_response.code
