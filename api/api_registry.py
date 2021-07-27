from models.api_meta_class import MetaAPI
from api.namespace import api_service_utility
from api.api_entity_id import APIGenerateID
from api.api_config_center import APIConfigCenter



class APIServiceIUtility(metaclass=MetaAPI):
    def api_registry(self):
        api_service_utility.add_resource(APIGenerateID, '/id')
        api_service_utility.add_resource(APIConfigCenter, '/config/<srv_namespace>')
