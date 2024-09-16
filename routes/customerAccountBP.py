from flask import Blueprint
from controllers.customerAccountController import save, getAll, login, getOne, updateCustomerAccount, deleteCustomerAccount

customerAccount_blueprint = Blueprint('user_bp', __name__)
customerAccount_blueprint.route('/', methods=['POST'])(save)
customerAccount_blueprint.route('/', methods=['GET'])(getAll)
customerAccount_blueprint.route('/login', methods=['POST'])(login)
customerAccount_blueprint.route('/get', methods=['GET'])(getOne)
customerAccount_blueprint.route('/update', methods=['PUT'])(updateCustomerAccount)
customerAccount_blueprint.route('/delete', methods=['DELETE'])(deleteCustomerAccount)