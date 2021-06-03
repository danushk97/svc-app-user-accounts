USER = '/user'


def test_create_user_given_valid_input_then_returns_data_with_status_code_200(client):
    response = client.post(USER, json={
        'email': 'email',
        'display_name': 'display_name',
        'phone_number': 1234567890,
        'password': 'password'
    })
    assert response.status_code == 200
    assert response.get_json() == {
        'user_id': '1234'
    }


def test_create_user_on_exception_from_service_layer_then_returns_data_with_status_code_500(client_raises_exception):
    response = client_raises_exception.post(USER, json={
        'email': 'email@gmail.com',
        'display_name': 'display_name',
        'phone_number': 1234567890,
        'password': 'password'
    })
    assert response.status_code == 500
    assert response.get_json() == {'error_codes': [{'error_code': 5000,
                                   'error_description': 'Internal server error'
                                   }]}
