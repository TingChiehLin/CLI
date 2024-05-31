from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from models import User, Booking, Restaurant

if __name__ == "__main__":
    engine = create_engine("sqlite:///yummy_sweet.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    fake = Faker()

    user = session.query(User).all()

    restaurants = []
    users = []

    user1 = User(
        name="Jay", email="jay@gmail.com", phone_number="04031425", note="No spicy food"
    )

    session.add(user1)
    session.commit()

    for i in range(6):
        restaurant = Restaurant(name=fake.unique.name(), rate=random.random(5))
        restaurants.append(restaurant)
        session.add(restaurant)
        session.commit()

    # booking Model
