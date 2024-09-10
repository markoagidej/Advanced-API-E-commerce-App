from sqlalchemy.orm import Session
from database import db
from models.customerAccount import CustomerAccount
from utils.util import encode_token

def save(customerAccount_data):
    with Session(db.engine) as session:
        with session.begin():
            new_customerAccount = CustomerAccount(username=customerAccount_data['username'], password=customerAccount_data['password'], role=customerAccount_data['role'])
            session.add(new_customerAccount)
            session.commit()

        session.refresh(new_customerAccount)
        return new_customerAccount
    
def getAll():
    with Session(db.engine) as session:
        customerAccounts = session.query(CustomerAccount).all()
        print(customerAccounts)
        return customerAccounts
    
def login_customer(username, password):
    customerAccount = (db.session.execute(db.select(CustomerAccount).where(CustomerAccount.username == username, CustomerAccount.password == password)).scalar_one_or_none())
    role_name = customerAccount.role
    if customerAccount:
        auth_token = encode_token(customerAccount.id, role_name)
        resp = {
            "status": "success",
            "message": "Successfully logged in",
            'auth_token': auth_token
        }
        return resp
    else:
        return None