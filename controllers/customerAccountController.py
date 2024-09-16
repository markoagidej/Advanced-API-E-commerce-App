from flask import request, jsonify
from models.schemas.customerAccountSchema import customerAccount_schema, customerAccounts_schema
from services import customerAccountService
from marshmallow import ValidationError
from utils.util import token_required, role_required
from caching import cache

@token_required
@role_required('admin')
def save():
    try:
        customerAccount_data = customerAccount_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customerAccount_save = customerAccountService.save(customerAccount_data)
    return customerAccount_schema.jsonify(customerAccount_save), 201

@cache.cached(timeout=5)
@token_required
@role_required('admin')
def getAll():
    try:
        customerAccounts = customerAccountService.getAll()
        return customerAccounts_schema.jsonify(customerAccounts), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    
def login():
    customer = request.json
    customerAccount = customerAccountService.login_customer(customer['username'], customer['password'])
    if customerAccount:
        return jsonify(customerAccount), 200
    else:
        resp = {
            "status": "Error",
            "message": "User does not exist"
        }
        return jsonify(resp), 404

@token_required
@role_required('admin')
def getOne():
    try:
        customer_data = customerAccountService.getOne(request.json)
        if customer_data:
            return customerAccount_schema.jsonify(customer_data), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@token_required
@role_required('admin')
def updateCustomerAccount():
    try:
        customer_data = customerAccountService.updateCustomerAccount(request.json)
        if customer_data:
            return customerAccount_schema.jsonify(customer_data), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@token_required
@role_required('admin')
def deleteCustomerAccount():
    try:
        customer_data = customerAccountService.deleteCustomerAccount(request.json)
        return customerAccount_schema.jsonify(customer_data), 201
    except ValidationError as err:
        return jsonify(err.messages), 400