from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

from datetime import datetime

db_url = "sqlite:///yummy_sweet.db"

engine = create_engine(db_url)

Base = declarative_base()

## A list of tables
class User(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(55))
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

# Create the database tables
Base.metadata.create_all(engine)