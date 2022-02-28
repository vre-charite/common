from .module_api import module_api
from .api_registry import APIServiceIUtility
from .api_entity_id import APIGenerateID, APIBulkGenerateID
from .api_config_center import APIConfigCenter

apis = [
    APIGenerateID(),
    APIBulkGenerateID()
]


def api_registry(apis):
    if len(apis) > 0:
        api = APIServiceIUtility()
        api.api_registry()
    else:
        print('[Fatal]', 'No API registered.')


api_registry(apis)
