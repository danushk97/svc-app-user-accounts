"""
This module holds the routes which is related add, update and delete user
account detail.
"""

from flask import Blueprint, request
from injector import inject
from apputils.http_verb import HttpVerb

from user_accounts.schema.user import CreateUserRequestSchema, CreateUserResponseSchema
from user_accounts.application.user_service import UserService


user_app = Blueprint('user', __name__, url_prefix='/user')


@inject
@user_app.route('', methods=[HttpVerb.POST])
def create_user(user_service: UserService):
    """
    Creates user.

    Args:
        user_service (UserService)

    Returns:
        user_id_info (dict):
            user_id (str): The id of the created user.
    """
    user_data = CreateUserRequestSchema().load(request.json or {})
    user = user_service.create_user(user_data)

    return CreateUserResponseSchema().dump(user)
