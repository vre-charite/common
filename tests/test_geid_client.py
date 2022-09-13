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

from common.geid.geid_client import GEIDClient


class TestGEIDClient:
    client = GEIDClient()

    def test_01_get_GEID(self):
        geid = self.client.get_GEID()
        assert type(geid) == str
        assert len(geid) == 47

    def test_02_get_bulk_GEID(self):
        geids = self.client.get_GEID_bulk(5)
        assert type(geids) == list
        assert len(geids) == 5
