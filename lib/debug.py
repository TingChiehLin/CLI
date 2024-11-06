import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User, Booking, Restaurant

db_url = "sqlite:////" + os.path.dirname(__file__) + "/db/yummy_sweet.db"

if __name__ == "__main__":
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb

    ipdb.set_trace()
