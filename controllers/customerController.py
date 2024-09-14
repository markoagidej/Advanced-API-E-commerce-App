from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from utils.util import role_required
from caching import cache

# @role_required('admin')
def save():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customer_save = customerService.save(customer_data)
    return customer_schema.jsonify(customer_save), 201

@cache.cache(timeout=5)
# @role_required('admin')
def getAll():
    try:
        customers = customerService.getAll()
        return customers_schema.jsonify(customers), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# @role_required('admin')
def getOne():
    try:
        customer_data = customerService.getOne(request.json)
        if customer_data:
            return customer_schema.jsonify(customer_data), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# @role_required('admin')
def updateCustomer():
    try:
        customer_data = customerService.updateCustomer(request.json)
        if customer_data:
            return customer_schema.jsonify(customer_data), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# @role_required('admin')
def deleteCustomer():
    try:
        customer_data = customerService.deleteCustomer(request.json)
        return customer_schema.jsonify(customer_data), 201
    except ValidationError as err:
        return jsonify(err.messages), 400