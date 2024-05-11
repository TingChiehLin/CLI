from db.models import engine, User
from sqlalchemy.orm import sessionmaker

from helpers import main_menu, menu_option

Session = sessionmaker(bind=engine)
session = Session()

def create_a_booking(name,email,note):
    pass

def main():

    bookingList = []
    choice = 0

    main_menu()
    while choice != 4:
        menu_option()
        choice = int(input("Please Enter your choice: "))
        if(choice == 0):
           print("inpt 0")
        elif(choice == 1):
            print("======================================")
            print("Are you exist users?")
            print("0 => Yes")
            print("1 => No")
        elif(choice == 2):
            print("Looking up for a booking")
        elif(choice == 3):
             print("Delete a booking")
        elif(choice == 4):
            print("Quit the application successfully!")
        else:
            print("Please input correct range number from 0 to 4")

if __name__ == "__main__":
    main()