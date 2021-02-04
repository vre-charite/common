from models.api_meta_class import MetaAPI
from api.namespace import api_service_utility
from api.api_entity_id import APIGenerateID



class APIServiceIUtility(metaclass=MetaAPI):
    def api_registry(self):
        api_service_utility.add_resource(APIGenerateID, '/id')
