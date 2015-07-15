import uuid

class Utils(object):
    @classmethod
    def get_uuid(cls):
        return uuid.uuid4()
    