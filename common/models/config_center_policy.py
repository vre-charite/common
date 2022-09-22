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

class ConfigCenterPolicy:
    @staticmethod
    def get_granted(srv_namespace):
        return {'service_download': ConfigCenterPolicy.service_download()}.get(srv_namespace, [])

    @staticmethod
    def service_download():
        return [
            'DOWNLOAD',
            'KEYCLOAK',
            'MINIO',
            'REDIS',
            'NEO4J_SERVICE',
            'PROVENANCE_SERVICE',
            'QUEUE_SERVICE',
            'UTILITY_SERVICE',
            'DATA_OPS_GR',
            'DATA_OPS_UTIL',
            'DATASET_SERVICE',
            'RDS_HOST',
            'RDS_PORT',
            'RDS_USER',
            'RDS_PWD',
            'RDS_DBNAME',
            'RDS_SCHEMA_DEFAULT',
            'OPEN_TELEMETRY_ENABLED',
            'CORE_ZONE_LABEL',
            'GREEN_ZONE_LABEL',
        ]
