from flask import request, jsonify
from models.schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError
from utils.util import token_required
from caching import cache

@token_required
def save():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    order_save = orderService.save(order_data)
    return order_schema.jsonify(order_save), 201

@cache.cached(timeout=5)
@token_required
def getAll():
    try:
        orders = orderService.getAll()
        return orders_schema.jsonify(orders), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@token_required
def find_all_pagination():
    page = request.args.get('page', 1 ,type=int)
    per_page = request.args.get('per_page', 10 ,type=int)
    return orders_schema.jsonify(orderService.find_all_pagination(page=page, per_page=per_page)), 200

@token_required
def getOne():
    try:
        order_data = orderService.getOne(request.json)
        if order_data:
            return order_schema.jsonify(order_data), 201
    except ValidationError as err:
        return jsonify(err.messages), 400