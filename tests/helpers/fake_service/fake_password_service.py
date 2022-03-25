import jwt

class FakePasswordService:
    def update_password(self, user_id, password):
        return None

    def validate_credential(self, user_id, password):
        return jwt.encode({'user_id': 'user_id'}, 'secret')


class FakePasswordServiceRaisesException:
    def update_password(self, user_id, password):
        raise Exception

    def validate_credential(self, user_id, password):
        raise Exception
