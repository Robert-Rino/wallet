class Unauthorized(Exception):
    def __init__(self, code: str='AUTH_ERROR'):
        self.code = code

