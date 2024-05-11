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
            email = int(input("Please Input your booking email"))
            for booking in bookingList:
                if email in booking:
                    print(booking)

            # isMember = int(input("Input 0 means you have not booked yet. Input 1 is already booked"))
            # if(isMember == 0):
            #     print("Make a new booking")
            # elif(isMember == 1):
            #     print("Please input your booking id")

        elif(choice == 2):
            print("Make a new booking")
            newBooking = ""
            bookingList.append(newBooking)
        elif(choice == 3):
             print("Delete a booking")
             removeID = int(input("Input your booking ID"))
             for booking in bookingList:
                if(removeID in booking):
                    print(removeID)
                else:
                    print("We can not find it")
        elif(choice == 4):
            print("Quit the application successfully!")
        else:
            print("Please input correct range number from 0 to 4")

if __name__ == "__main__":
    main()