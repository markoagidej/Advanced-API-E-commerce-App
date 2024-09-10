from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class CustomerAccountManagementRole(Base):
    __tablename__ = "customerAccount_management_roles"
    id: Mapped[int] = mapped_column(primary_key=True)
    customerAccount_management_id: Mapped[int] = mapped_column(db.ForeignKey('customerAccounts.id'))
    role_id: Mapped[int] = mapped_column(db.ForeignKey('roles.id'))