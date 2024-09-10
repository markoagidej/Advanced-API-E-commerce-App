from marshmallow import fields
from schema import ma

class CustomerAccountSchema(ma.Schema):
    id = fields.Integer(required=False)
    username = fields.String(required=True)
    password = fields.String(required=True)
    role = fields.String(required=True)

class Meta:
    fields = ('id', 'username', 'password', 'role')

customerAccount_schema = CustomerAccountSchema()
customerAccounts_schema = CustomerAccountSchema(many=True)