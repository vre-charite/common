from common.services.logger_services.logger_factory_service import SrvLoggerFactory
from common.models.service_id_generator import GenerateId


class GEIDClient():
    _logger = SrvLoggerFactory('geid_client').get_logger()

    def get_GEID(self) -> str:
        self._logger.info(f"Generate GEID without data type")
        new_id = GenerateId()
        uniq_id = new_id.generate_id() + '-' + new_id.time_hash()
        return uniq_id

    def get_GEID_bulk(self, number: int) -> list:
        self._logger.info(f"Generate GEID without data type")
        id_list = []
        for _ in range(number):
            new_id = GenerateId()
            uniq_id = new_id.generate_id() + '-' + new_id.time_hash()
            id_list.append(uniq_id)
        return id_list
