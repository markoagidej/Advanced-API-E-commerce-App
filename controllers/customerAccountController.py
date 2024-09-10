from flask import request, jsonify
from models.schemas.customerAccountSchema import customerAccount_schema, customerAccounts_schema
from services import customerAccountService
from marshmallow import ValidationError
from utils.util import role_required

def save():
    try:
        customerAccount_data = customerAccount_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customerAccount_save = customerAccountService.save(customerAccount_data)
    return customerAccount_schema.jsonify(customerAccount_save), 201

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