"""
This module holds the routes which is related add, update and delete user
account detail.
"""

from appscommon.http import send_success_response
from appscommon.http.middleware import error_filter 
from flask import Blueprint, request

from useraccounts.schemas.account import CreateAccountRequestSchema
from useraccounts.application.service import AccountService 
from useraccounts.bootstrap import bootstrap
from useraccounts.constants import Constants
from useraccounts.app import api_spec


accounts_app = Blueprint('account', __name__, url_prefix='/accounts')
services = bootstrap()


@accounts_app.post('create')
@error_filter
@api_spec.validate(body=CreateAccountRequestSchema)
def create_account():
    """Creates account.
    """
    account_service: AccountService = services[Constants.ACCOUNT_SERVICE]()
    result = account_service.create_account(request.context.body.dict())

    return send_success_response(result)
