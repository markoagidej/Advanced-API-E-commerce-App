from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from database import db
from models.product import Product
from caching import cache

def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data['name'], price=product_data['price'])
            session.add(new_product)
            session.commit()

        session.refresh(new_product)
        return new_product
    
@cache.cached(timeout=5)
def getAll():
    with Session(db.engine) as session:
        products = session.query(Product).all()
        print(products)
        return products
    
@cache.cached(timeout=5)
def find_all_pagination(page=1, per_page=1):
    products = db.paginate(select(Product), page=page, per_page=per_page)
    return products

@cache.cached(timeout=5)
def getOne(id_data):
    product = db.session.execute(db.select(Product).where(Product.id == id_data["id"])).scalar_one_or_none()
    if product:
        return product
    else:
        return None

def updateProduct(new_data):
    old_product = db.session.execute(db.select(Product).where(Product.id == new_data['id'])).scalar_one_or_none()
    if old_product:
        db.session.execute(update(Product).where(Product.id == new_data['id']).values(name=new_data['name'], price=new_data['price']))
        new_product = db.session.execute(db.select(Product).where(Product.id == new_data['id'])).scalar_one_or_none()
        db.session.commit()
        return new_product
    else:
        return None

def deleteProduct(id_data):
    product = db.session.execute(db.select(Product).where(Product.id == id_data["id"])).scalar_one_or_none()
    if product:
        db.session.execute(delete(Product).where(Product.id == id_data["id"]))
        db.session.commit()
        return product
    else:
        return None