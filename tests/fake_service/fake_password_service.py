from logging import raiseExceptions


class FakePasswordService:
    def update_password(self, user_id, password):
        return None

    def validate_credential(self, user_id, password):
        return None


class FakePasswordServiceRaisesException:
    def update_password(self, user_id, password):
        raise Exception

    def validate_credential(self, user_id, password):
        raise Exception
