import jwt

def test_login_given_valid_input_then_returns_data_with_status_code_200(client, monkeypatch):
    response = client.post('/login', json={
        'user_id': 'id',
        'password': 'password'
    })

    decoded_jwt = jwt.decode(response.headers['set-cookie'], 'secret', algorithms=['HS256'])
    assert decoded_jwt == {'user_id': 'user_id'}
    assert response.status_code == 200
    assert response.get_json() == {
        'message': 'Login successful'
    }


def test_login_on_exception_from_service_layer_returns_status_code_500(client_raises_exception):
    response = client_raises_exception.post('/login', json={
        'user_id': 'user_id',
        'password': 'password'
    })
    assert response.status_code == 500
    assert response.get_json() == {'error_codes': [{'error_code': 5000, 'error_description': 'Internal server error'}]}
