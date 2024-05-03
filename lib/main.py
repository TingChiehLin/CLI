from db.models import engine, User
from sqlalchemy.orm import sessionmaker

import click

Session = sessionmaker(bind=engine)
session = Session()



@click.command()
@click.option("--name", prompt="Your booking name", help="The booking name of table")
@click.option("--email", prompt="Your booking email", help="The booking name of table")
@click.option("--note", prompt="Your booking note", help="The booking name of table")
def create_user(name,email,note):
    pass

def main():
    print("Hello There! Welcome to Yummy Sweet Restaurant Booking CLI App")
    print("Please Input number to chose next step")
    create_user()

if __name__ == "__main__":
    main()