import uuid
import time


class GenerateId:

    def generate_id(self):
        return str(uuid.uuid1())

    def time_hash(self):
        return str(time.time())[0:10]
