"""
This module holds the routes which is related add, update and delete user
account detail.
"""

from flask import Blueprint
from pydantic_webargs import webargs
from common.http import send_success_response
from common.http.middleware import error_filter 

from useraccounts.schemas.account import CreateAccountRequestSchema
from useraccounts.application.service import AccountService 
from useraccounts.bootstrap import bootstrap
from useraccounts.constants import Constants


accounts_app = Blueprint('account', __name__, url_prefix='/accounts')
services = bootstrap()


@accounts_app.route('create', methods=['post'])
@error_filter
@webargs(body=CreateAccountRequestSchema)
def create_account(**kwargs: dict):
    """
    Creates account.
    """
    account_service: AccountService = services[Constants.ACCOUNT_SERVICE]()
    result = account_service.create_account(kwargs[Constants.PAYLOAD])

    return send_success_response(result)
