"""
This module holds the routes which helps to update user password.
"""

from flask import Blueprint, request
from user_accounts.application.password_service import PasswordService
from user_accounts.common.constants import Constants
from apputils.http_verb import HttpVerb


password_app = Blueprint('password', __name__, url_prefix='/password')


@password_app.route('', methods=[HttpVerb.PUT])
def update_password(password_service: PasswordService):
    request_json = request.json or {}
    user_id = str(request_json.get(Constants.USER_ID, '')).strip()
    password = str(request_json.get(Constants.PASSWORD, '')).strip()
    password_service.update_password(user_id, password)

    return {
        'message': 'Password updated successfully'
    }
