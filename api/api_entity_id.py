from flask_restx import Resource, fields
from flask import request
from services.logger_services.logger_factory_service import SrvLoggerFactory
from models.service_id_generator import GenerateId
from api_response import APIResponse, EAPIResponseCode
from api.namespace import api_service_utility

get_return = """
            {
                "code": 200,
                "error_msg": "",
                "result": "nfs-9a37ae44-6264-11eb-ae2d-c9838b13797a-1611946978"
            }
            """

get_error = """
            {
                "code": 400,
                "error_msg": "entity_type is required",
                "result": ""
            }
            """

class APIGenerateID(Resource):
    _logger = SrvLoggerFactory('api_generate_id').get_logger()
    @api_service_utility.doc(params={'entity_type': 'Entity type'})
    @api_service_utility.response(200, get_return)
    @api_service_utility.response(400, get_error)
    def get(self):
        """Generate a unique id, which is entity_type + uuid + timestamp"""
        entity_type = request.args.get("entity_type")
        self._logger.info(f"Received entity type: {entity_type}")
        api_response = APIResponse()
        try:
            if not entity_type or entity_type == '':
                api_response.set_code(EAPIResponseCode.bad_request)
                api_response.set_error_msg("entity_type is required")
                return api_response.to_dict, api_response.code
            else:
                new_id = GenerateId()
                entity_type = str(entity_type)
                uniq_id = entity_type + '-' + new_id.generate_id() + '-' + new_id.time_hash()
                api_response.set_code(EAPIResponseCode.success)
                api_response.set_result(uniq_id)
                return api_response.to_dict, api_response.code
        except Exception as e:
            self._logger.error(f"ERROR HAPPENED: {e}")
            api_response.set_code(EAPIResponseCode.internal_error)
            api_response.set_result(e)
            return api_response.to_dict, api_response.code

