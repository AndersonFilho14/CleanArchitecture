from src.validators.user_register_validator import user_register_validator

class MockRequest:
    def __init__(self):
        self.json = None

def test_user_register_validator():
    request = MockRequest()
    request.json = {
        "first_name": "asd",
        "last_name": "aasd",
        "age": 15
        }

    user_register_validator(request)
