from user_accounts.common.constants import Constants


def test_constants_no_action_on_rebinding_value():
    assert Constants.PHONE_NUMBER == 'phone_number'
    Constants.PHONE_NUMBER = 12344
    assert Constants.PHONE_NUMBER == 'phone_number'
