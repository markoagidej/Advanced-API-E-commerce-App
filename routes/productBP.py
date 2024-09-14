from flask import Blueprint
from controllers.productController import save, getAll, find_all_pagination, getOne, updateProduct, deleteProduct

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/', methods=['GET'])(getAll)
product_blueprint.route('/paginate', methods=['GET'])(find_all_pagination)
product_blueprint.route('/get', methods=['GET'])(getOne)
product_blueprint.route('/update', methods=['PUT'])(updateProduct)
product_blueprint.route('/delete', methods=['DELETE'])(deleteProduct)