import jwt


class FakeAuthService:
    def login(self, login_data):
        return jwt.encode({'user_id': 'user_id'}, 'secret')

class FakeAuthServiceRaisesException:
    def login(self, login_data):
        raise Exception
