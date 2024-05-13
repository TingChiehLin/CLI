from sqlalchemy import ForeignKey, Column, Integer, Float, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref
# from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class User(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(55))
    phone_number = Column(String())
    note = Column(String)

    bookings = relationship('Booking',backref=backref("user"))

    def __repr__(self):
        return f"User {self.id}: " \
            + f"Name {self.name}, " \
            + f"Email: {self.email}"

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    time = Column(DateTime(), default=datetime.now())
    date = Column(String)
    user_id = Column(Integer(), ForeignKey('user.id'))

    def __repr__(self):
        return f"Booking: {self.id} " \
              + f"Time: {self.time}" \
              + f"Date: {self.date}"

class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True)
    code = Column(String)
    # user_id = Column(Integer(),ForeignKey('user_id'))

class MenuItem(Base):
    __tablename__ = "menu_item"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float(2))

    def __init__(self, id, name,price):
        self.id = None
        self.name = name
        self.price = price

# Create the database tables
# Base.metadata.create_all(engine)