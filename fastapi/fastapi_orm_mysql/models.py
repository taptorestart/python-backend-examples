from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from database import Base


'''
# Default
from sqlalchemy import Integer
Integer: signed integer, length 11

# MySQL
from sqlalchemy.dialects.mysql import INTEGER
INTEGER: signed integer, length 11
INTEGER(unsigned=True): unsigned integer, length 10
INTEGER(display_width=11, unsigned=True): unsigned integer, length 11

source: https://docs.sqlalchemy.org/en/14/dialects/mysql.html?highlight=unsigned#sqlalchemy.dialects.mysql.INTEGER.params.unsigned
'''


class User(Base):
    __tablename__ = "users"

    id = Column(INTEGER(display_width=11, unsigned=True), primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(INTEGER(display_width=11, unsigned=True), primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True)
    owner_id = Column(INTEGER(display_width=11, unsigned=True), ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
