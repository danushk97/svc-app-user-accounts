def test_update_password_given_valid_input_then_returns_data_with_status_code_200(client):
    response = client.put('/password', json={
        'user_id': 'id',
        'password': 'password'
    })
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Password updated successfully'}


def test_update_password_on_exception_from_service_layer_returns_status_code_500(client_raises_exception):
    response = client_raises_exception.put('/password', json={
        'user_id': 'user_id',
        'password': 'password'
    })
    assert response.status_code == 500
    assert response.get_json() == {'error_codes': [{'error_code': 5000, 'error_description': 'Internal server error'}]}
