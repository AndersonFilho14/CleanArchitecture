class HttpBadRequestError(Exception):
    def __init__(self, message: str)-> None:
        super().__init__(message)
        self.message: str = message
        self.name: str = "BadRequest"
        self.status_code: int = 400
