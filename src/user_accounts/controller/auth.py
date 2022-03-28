"""
This module holds the routes which helps to valdiate credential.
"""

from flask import Blueprint, request, make_response
from apputils.http_verb import HttpVerb

from user_accounts.application.password_service import PasswordService
from user_accounts.common.constants import Constants


auth_app = Blueprint('auth', __name__, url_prefix='/login')


@auth_app.route('', methods=[HttpVerb.POST])
def login(password_service: PasswordService):
    request_json = request.json or {}
    email = str(request_json.get(Constants.EMAIL, '')).strip()
    password = str(request_json.get(Constants.PASSWORD, '')).strip()
    jwt_token = password_service.validate_credential(email, password)
    response = make_response({
        'message': 'Login successful'
    })
    response.set_cookie(jwt_token)

    return response
