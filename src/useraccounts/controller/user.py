"""
This module holds the routes which is related add, update and delete user
account detail.
"""

from flask import Blueprint
from pydantic_webargs import webargs
from common.http import send_success_response
from common.http.middleware import error_filter 

from useraccounts.schema.user import CreateUserRequestSchema
from useraccounts.application.service import UserService
from useraccounts.bootstrap import bootstrap


user_app = Blueprint('user', __name__, url_prefix='/user')
services = bootstrap()


@user_app.route('', methods=['post'])
@error_filter
@webargs(body=CreateUserRequestSchema)
def create_user(payload: CreateUserRequestSchema, query=None):
    """
    Creates user.

    Args:
        hashing_itertation (CreateUserAccountRequestSchema): Request payload.

    Returns:
        
    """
    user_service: UserService = services["user_service"]()
    result = user_service.create_user(payload)

    return send_success_response(result)
