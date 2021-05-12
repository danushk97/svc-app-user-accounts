import pytest


from user_accounts.application.preprocessor.data_preprocessor import \
    DataPreprocessor

@pytest.mark.parametrize('test_input, expected',
                     [('String', 'string'),
                     ('String   ', 'string')])
def test_strip_and_lower_given_valid_string_then_returns_lower_cased_stripped_string(test_input, expected):
    assert DataPreprocessor.strip_and_lower(test_input) == expected
