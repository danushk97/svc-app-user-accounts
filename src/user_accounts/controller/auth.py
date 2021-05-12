"""
This module holds the routes which helps to valdiate credential.
"""

from flask import Blueprint, request
from user_accounts.application.password_service import PasswordService
from user_accounts.common.constants import Constants
from apputils.http_verb import HttpVerb


auth_app = Blueprint('auth', __name__, url_prefix='/login')


@auth_app.route('', methods=[HttpVerb.POST])
def login(password_service: PasswordService):
    request_json = request.json or {}
    email = str(request_json.get(Constants.EMAIL, '')).strip()
    password = str(request_json.get(Constants.PASSWORD, '')).strip()
    password_service.validate_credential(email, password)

    return {
        'message': 'Login successful'
    }
