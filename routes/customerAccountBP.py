from flask import Blueprint
from controllers.customerAccountController import save, getAll, login

customerAccount_blueprint = Blueprint('user_bp', __name__)
customerAccount_blueprint.route('/', methods=['POST'])(save)
customerAccount_blueprint.route('/', methods=['GET'])(getAll)
customerAccount_blueprint.route('/login', methods=['POST'])(login)