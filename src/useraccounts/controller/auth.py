"""
This module holds the routes which helps to valdiate credential.
"""

from flask import Blueprint, request, make_response
from useraccounts.application.auth_service import AuthService
from apputils.http_verb import HttpVerb

from useraccounts.schema.auth import LoginRequestSchema
from useraccounts.application.password_service import PasswordService
from useraccounts.common.constants import Constants


auth_app = Blueprint('auth', __name__, url_prefix='/login')


@auth_app.route('', methods=[HttpVerb.POST])
def login(auth_service: AuthService):
    login_data = LoginRequestSchema().load(request.json or {})
    jwt_token = auth_service.login(login_data)
    response = make_response({
        'message': 'Login request was successful.'
    })
    response.set_cookie(jwt_token)

    return response
