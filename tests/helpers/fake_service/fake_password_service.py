class FakePasswordService:
    def update_password(self, user_id, password):
        return None


class FakePasswordServiceRaisesException:
    def update_password(self, user_id, password):
        raise Exception
