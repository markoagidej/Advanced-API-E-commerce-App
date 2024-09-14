from flask import Blueprint
from controllers.customerController import save, getAll, getOne, updateCustomer, deleteCustomer

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(getAll)
customer_blueprint.route('/get', methods=['GET'])(getOne)
customer_blueprint.route('/update', methods=['PUT'])(updateCustomer)
customer_blueprint.route('/delete', methods=['DELETE'])(deleteCustomer)