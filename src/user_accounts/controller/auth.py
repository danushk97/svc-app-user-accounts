"""
This module holds the routes which helps to valdiate credential.
"""

from flask import Blueprint, request, make_response
from user_accounts.schema.auth import LoginRequestSchema
from apputils.http_verb import HttpVerb

from user_accounts.application.password_service import PasswordService
from user_accounts.common.constants import Constants


auth_app = Blueprint('auth', __name__, url_prefix='/login')


@auth_app.route('', methods=[HttpVerb.POST])
def login(password_service: PasswordService):
    auth_data = LoginRequestSchema().load(request.json or {})
    jwt_token = password_service.validate_credential(
        auth_data[Constants.EMAIL],
        auth_data[Constants.PASSWORD]
    )
    response = make_response({
        'message': 'Login request was successful.'
    })
    response.set_cookie(jwt_token)

    return response
