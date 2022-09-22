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

from common.models.service_id_generator import GenerateId


class GEIDClient:
    def get_GEID(self) -> str:
        new_id = GenerateId()
        uniq_id = new_id.generate_id() + '-' + new_id.time_hash()
        return uniq_id

    def get_GEID_bulk(self, number: int) -> list:
        id_list = []
        for _ in range(number):
            new_id = GenerateId()
            uniq_id = new_id.generate_id() + '-' + new_id.time_hash()
            id_list.append(uniq_id)
        return id_list
