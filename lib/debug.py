from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User, Booking

if __name__ == "__main__":
    db_url = "sqlite:////Users/JayLinXR/Desktop/python-p3-cli-project-template/lib/db/yummy_sweet.db"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb

    ipdb.set_trace()
