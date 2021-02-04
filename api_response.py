from enum import Enum
import copy


class EAPIResponseCode(Enum):
    success = 200
    internal_error = 500
    bad_request = 400
    not_found = 404
    forbidden = 403
    conflict = 409
    accepted = 202
    unauthorized = 401


class APIResponse:
    def __init__(self):
        self._attribute_map = {
            'code': EAPIResponseCode.success.value,  ## by default success
            'error_msg': '',  ## empty when success
            'result': '',
        }

    @property
    def to_dict(self):
        return self._attribute_map

    @property
    def code(self):
        return self._attribute_map['code']

    @property
    def error_msg(self):
        return self._attribute_map['code']

    @property
    def result(self):
        return self._attribute_map['result']

    def set_code(self, code: EAPIResponseCode):
        self._attribute_map['code'] = code.value

    def set_error_msg(self, error_msg: str):
        self._attribute_map['error_msg'] = error_msg

    def set_result(self, result):
        self._attribute_map['result'] = result
