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

from datetime import datetime

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

restaurant_user = Table(
    "restaurant_user",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("restaurant_id", ForeignKey("restaurant_id.id"), primary_key=True),
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
    # restaurants = relationship(
    #     "Restaurant", secondary=restaurant_user, back_populates="users"
    # )

    def __repr__(self):
        return f"User {self.id}: " + f"Name {self.name}, " + f"Email: {self.email}"


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    time = Column(DateTime(), default=datetime.now())
    date = Column(String)

    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    user_id = Column(Integer(), ForeignKey("users.id"))
    restaurant_id = Column(Integer(), ForeignKey("restaurant.id"))

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

    # bookings = relationship("Booking", backref=backref("restaurant"))
    # users = relationship(
    #     "User", secondary=restaurant_user, back_populates="restaurants"
    # )

    def __repr__(self):
        return (
            f"Restaurant(id:{self.id},)" + f"Name: {self.name}" + f"rate:{self.rate},"
        )
