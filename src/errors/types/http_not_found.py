class HttpNotFoundError(Exception):
    def __init__(self, message: str)-> None:
        super().__init__(message)
        self.message: str = message
        self.name: str = "NotFound"
        self.status_code: int = 404
