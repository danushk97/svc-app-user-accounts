# def test_update_password_given_valid_input_then_returns_data_with_status_code_200(client):
#     response = client.put('/user/password', json={
#         'user_id': 'id',
#         'password': 'password'
#     })
#     assert response.status_code == 200
#     assert response.get_json() == {'message': 'Password updated successfully'}


# def test_update_password_on_exception_from_service_layer_returns_status_code_500(client_raises_exception):
#     response = client_raises_exception.put('/user/password', json={
#         'user_id': 'user_id',
#         'password': 'password'
#     })
#     assert response.status_code == 500
#     assert response.get_json() == {'error': {'code': 500, 'message': 'Internal server error'}}


# def test_update_password_given_invalid_user_id_returns_400(client):
#     response = client.put('/user/password', json={
#         'user_id': '',
#         'password': 'password'
#     })
#     assert response.status_code == 400
#     assert response.get_json() == {
#         'error': {
#             'code': 400,
#             'errors': [
#                 {
#                     'field': 'user_id',
#                     'message': 'Please provide a valid user_id.'
#                 }
#             ],
#             'message': 'Payload contains missing or invalid data.'
#         }
#     }


# def test_update_password_given_invalid_password_raises_invalid_password_exception(client):
#     response = client.put('/user/password', json={
#         'user_id': 'test_id',
#         'password': 'invalid'
#     })
#     assert response.status_code == 400
#     assert response.get_json() == {
#         'error': {
#             'code': 400,
#             'errors': [
#                 {
#                     'field': 'password',
#                     'message': 'password length must be between 8 and 40.'
#                 }
#             ],
#             'message': 'Payload contains missing or invalid data.'
#         }
#     }
