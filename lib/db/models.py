from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Column,
    Integer,
    String,
    DateTime,
    MetaData,
    Table,
    func,
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

restaurant_user = Table(
    "restaurant_users",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("restaurant_id", ForeignKey("restaurants.id"), primary_key=True),
    extend_existing=True,
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(55))
    phone_number = Column(String())
    note = Column(String)

    bookings = relationship("Booking", backref=backref("user"))
    restaurants = relationship(
        "Restaurant", secondary=restaurant_user, back_populates="users"
    )

    def __init__(self, name, email, phone_number, note, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.note = note

    def __repr__(self):
        return f"User {self.id}: " + f"Name {self.name}, " + f"Email: {self.email}"


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    time = Column(String)
    date = Column(String)

    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), default=func.now(), onupdate=func.now())

    user_id = Column(Integer(), ForeignKey("users.id"))
    restaurant_id = Column(Integer(), ForeignKey("restaurants.id"))

    def __init__(self, time, date, id=None):
        self.id = id
        self.time = time
        self.date = date

    def __repr__(self):
        return f"Booking: {self.id} " + f"Time: {self.time}" + f"Date: {self.date}"


# many to many
# user can book many restaurants
# a restaurant can have many users

# one to many
# a booking belongs to a restaurant
# a restaurant can have many bookings


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer(), primary_key=True)
    name = Column(String)
    rate = Column(Integer())

    bookings = relationship("Booking", backref=backref("restaurant"))
    users = relationship(
        "User", secondary=restaurant_user, back_populates="restaurants"
    )

    def __init__(self, name, rate, id=None):
        self.name = name
        self.rate = rate

    def __repr__(self):
        return (
            f"Restaurant(id:{self.id},)" + f"Name: {self.name}" + f"rate:{self.rate},"
        )
