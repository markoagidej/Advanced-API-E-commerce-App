from sqlalchemy.orm import Session
from sqlalchemy import delete, update
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
    
def getOne(id_data):
    account = db.session.execute(db.select(CustomerAccount).where(CustomerAccount.id == id_data["id"])).scalar_one_or_none()
    if account:
        return account
    else:
        return None

def updateCustomerAccount(new_data):
    old_account = db.session.execute(db.select(CustomerAccount).where(CustomerAccount.id == new_data['id'])).scalar_one_or_none()
    if old_account:
        db.session.execute(update(CustomerAccount).where(CustomerAccount.id == new_data['id']).values(username=new_data['username'], password=new_data['password'], role=new_data['role']))
        new_account = db.session.execute(db.select(CustomerAccount).where(CustomerAccount.id == new_data['id'])).scalar_one_or_none()
        db.session.commit()
        return new_account
    else:
        return None

def deleteCustomerAccount(id_data):
    account = db.session.execute(db.select(CustomerAccount).where(CustomerAccount.id == id_data["id"])).scalar_one_or_none()
    if account:
        db.session.execute(delete(CustomerAccount).where(CustomerAccount.id == id_data["id"]))
        db.session.commit()
        return account
    else:
        return None