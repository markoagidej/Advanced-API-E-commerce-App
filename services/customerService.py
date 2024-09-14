from sqlalchemy.orm import Session
from sqlalchemy import delete, update
from database import db
from models.customer import Customer

def save(customer_data):
    with Session(db.engine) as session:
        with session.begin():
            new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'])
            session.add(new_customer)
            session.commit()

        session.refresh(new_customer)
        return new_customer
    
def getAll():
    with Session(db.engine) as session:
        customers = session.query(Customer).all()
        return customers
    
def getOne(id_data):
    customer = db.session.execute(db.select(Customer).where(Customer.id == id_data["id"])).scalar_one_or_none()
    if customer:
        return customer
    else:
        return None

def updateCustomer(new_data):
    old_customer = db.session.execute(db.select(Customer).where(Customer.id == new_data['id'])).scalar_one_or_none()
    if old_customer:
        db.session.execute(update(Customer).where(Customer.id == new_data['id']).values(name=new_data['name'], email=new_data['email'], phone=new_data['phone']))
        new_customer = db.session.execute(db.select(Customer).where(Customer.id == new_data['id'])).scalar_one_or_none()
        db.session.commit()
        return new_customer
    else:
        return None

def deleteCustomer(id_data):
    customer = db.session.execute(db.select(Customer).where(Customer.id == id_data["id"])).scalar_one_or_none()
    if customer:
        db.session.execute(delete(Customer).where(Customer.id == id_data["id"]))
        db.session.commit()
        return customer
    else:
        return None