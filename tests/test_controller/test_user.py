USER = '/user'


def test_create_user_given_valid_input_then_returns_data_with_status_code_200(client):
    response = client.post(USER, json={
        'attr': {
            'email': 'email@gmail.com',
            'display_name': 'display_name'
        },
        'password': 'password'
    })
    assert response.status_code == 200
    assert response.get_json() == {
        'user_id': '1234'
    }


def test_create_user_on_exception_from_service_layer_then_returns_data_with_status_code_500(client_raises_exception):
    response = client_raises_exception.post(USER, json={
        'attr': {
            'email': 'email@gmail.com',
            'display_name': 'display_name'
        },
        'password': 'password'
    })
    assert response.status_code == 500
    assert response.get_json() == {'error': {'code': 500, 'message': 'Internal server error'}}


def test_create_user_given_invalid_user_data_returns_400(client):
    response = client.post(USER, json={
        'password': 'password',
        'attr': {}
    })
    assert response.status_code == 400
    response_json = response.get_json()
    response_json['error']['errors'] = sorted(response_json['error']['errors'], key=lambda x: x['field'])
    assert response_json == {
        'error': {
            'code': 400,
            'errors': [
                {'field': 'display_name', 'message': 'display_name is required.'},
                {'field': 'email', 'message': 'email is required.'}
            ],

            'message': 'Payload contains missing or invalid data.'
        }
    }


def test_create_user_given_invalid_password_returns_400(client):
    response = client.post(USER, json={
        'attr':{
            'email': 'email@gmail.com',
            'display_name': 'name',
        }
    })
    assert response.status_code == 400
    assert response.get_json()['error'] == {
        'code': 400,
        'errors': [
            {
                'field': 'password',
                'message': 'password is required.'
            }
        ],
        'message': 'Payload contains missing or invalid data.'
    }


def test_create_user_given_invalid_password_length_returns_400(client):
    response = client.post(USER, json={
        'attr':{
            'email': 'email@gmail.com',
            'display_name': 'name',
        },
        'password': '123'
    })
    assert response.status_code == 400
    assert response.get_json() == {
        'error': {
            'code': 400,
            'errors': [
                {
                    'field': 'password',
                    'message': 'password length must be between 8 and 40.'
                }
            ],
            'message': 'Payload contains missing or invalid data.'
        }
    }
