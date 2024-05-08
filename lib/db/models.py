from sqlalchemy import create_engine, ForeignKey, Column, Integer, Float, String, DateTime, MetaData
# from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

db_url = "sqlite:///yummy_sweet.db"

metadata = MetaData(naming_convention=convention)

engine = create_engine(db_url)

Base = declarative_base(metadata=metadata)

class User(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(55))
    phone_number = Column(String())
    note = Column(String)

    def __repr__(self):
        return f"User {self.id}: " \
            + f"Name {self.name}, " \
            + f"Email: {self.email}"

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    time = Column(DateTime(), default=datetime.now())
    date = Column(String)
    user_id = Column(Integer)

    def __repr__(self):
        return f"Booking: {self.id} " \
              + f"Time: {self.time}" \
              + f"Date: {self.date}"

class Coupon(Base):
    __tablename__ = "coupons"
    id = Column(Integer, primary_key=True)
    code = Column(String)
    user_id = Column(Integer)

class MenuItem(Base):
    def __init__(self, id, name,price):
        self.id = None
        self.name = name
        self.price = price

    __tablename__ = "menu_item"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float(2))

# Create the database tables
Base.metadata.create_all(engine)