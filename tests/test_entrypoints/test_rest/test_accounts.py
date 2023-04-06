from dataclasses import asdict


CREATE_ACCOUNT = '/accounts/create'


def test_create_user_given_valid_input_then_returns_data_with_status_code_201(test_client, account_schema_instance):
    request_payload = asdict(account_schema_instance)
    request_payload['password'] = 'test password'
    response = test_client.post(CREATE_ACCOUNT, json=request_payload)
    assert response.status_code == 201


def test_create_user_given_invalid_passoword_returns_400(test_client, account_schema_instance):
    request_payload = asdict(account_schema_instance)
    request_payload['password'] = 'tes'  # minimum password length is 4
    response = test_client.post(CREATE_ACCOUNT, json=request_payload)
    assert response.status_code == 400
    assert response.json['title'] == 'Validation error'
    assert response.json['invalid_params'] == [{'field': ['password'], 'msg': 'ensure this value has at least 4 characters'}]

# def test_create_user_on_exception_from_service_layer_then_returns_data_with_status_code_500(client_raises_exception):
#     response = client_raises_exception.post(CREATE_ACCOUNT, json={
#         'attr': {
#             'email': 'email@gmail.com',
#             'display_name': 'display_name'
#         },
#         'password': 'password'
#     })
#     assert response.status_code == 500
#     assert response.get_json() == {'error': {'code': 500, 'message': 'Internal server error'}}


# def test_create_account_given_invalid_data_returns_400(test_client):
#     response = test_client.post(CREATE_ACCOUNT, json={
#         'password': 'password'
#     })
#     assert response.status_code == 400
#     response_json = response.get_json()
#     response_json['error']['errors'] = sorted(response_json['error']['errors'], key=lambda x: x['field'])
#     assert response_json == {
#         'error': {
#             'code': 400,
#             'errors': [
#                 {'field': 'display_name', 'message': 'display_name is required.'},
#                 {'field': 'email', 'message': 'email is required.'}
#             ],

#             'message': 'Payload contains missing or invalid data.'
#         }
#     }


def test_create_account_given_missing_fields_returns_400(test_client):
    response = test_client.post(CREATE_ACCOUNT, json={
            'email': 'email@gmail.com',
            'display_name': 'name',
        }
    )
    assert response.status_code == 400
    assert response.get_json()['invalid_params'] == [
        {
            "field": [
                key
            ],
            "msg": "field required"
        }
        for key in ["name", "dob", "username", "password"]
    ]
