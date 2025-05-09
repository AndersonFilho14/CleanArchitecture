from src.validators.user_finder_validator import user_finder_validator

class MockRequest:
    def __init__(self):
        self.args = None

def test_user_finder_validator():
    request = MockRequest()
    request.args = {
        "first_name": "123"
        }

    user_finder_validator(request)
