class FakeUserService:
    def create_user(self, user_info: dict):
        return {
            'user_id': '1234'
        }


class FakeUserServiceRaisesException:
    def create_user(self, user_info: dict):
        raise Exception
