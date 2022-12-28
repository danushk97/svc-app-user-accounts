# """
# This module holds the routes which helps to update user password.
# """

# from flask import Blueprint, request
# from apputils.http_verb import HttpVerb

# from useraccounts.schema.password import UpdatePasswordRequestSchema
# from useraccounts.application.password_service import PasswordService
# from src.useraccounts.constants import Constants


# password_app = Blueprint('password', __name__, url_prefix='/user/password')


# @password_app.route('', methods=[HttpVerb.PUT])
# def update_password(password_service: PasswordService):
#     update_password_data = UpdatePasswordRequestSchema().load(request.json or {})
#     password_service.update_password(
#         update_password_data[Constants.USER_ID],
#         update_password_data[Constants.PASSWORD]
#     )

#     return {
#         'message': 'Password updated successfully'
#     }
