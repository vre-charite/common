from common.models.api_meta_class import MetaAPI
from common.api.namespace import api_service_utility
from common.api.api_entity_id import APIGenerateID, APIBulkGenerateID
from common.api.api_config_center import APIConfigCenter


class APIServiceIUtility(metaclass=MetaAPI):
    def api_registry(self):
        api_service_utility.add_resource(APIGenerateID, '/id')
        api_service_utility.add_resource(APIBulkGenerateID, '/id/batch')
        api_service_utility.add_resource(APIConfigCenter, '/config/<srv_namespace>')
