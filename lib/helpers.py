import os
from sqlalchemy  import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User

db_url = "sqlite:///yummy_sweet.db"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

def clear_screen():
    clearscreen = lambda: os.system('clear')
    clearscreen(0)

def main_menu():
    print("============================================================================")
    print("Hello There! Welcome to Yummy Sweet Restaurant CLI App")
    print("Developed by Jay Lin")
    print("============================================================================")

def menu_option():
    print("Please choose what you want to do")
    print("Input 1 - View booking details")
    print("Input 2 - Make a new booking")
    print("Input 3 - Delete a booking")
    print("Input 4 - Quit")

def prompt_input():
    menu_option()
    choice = int(input("Please Enter your choice: "))
    if (choice <= 4):
        return choice
    else:
        print("Please input correct range number from 1 to 4")
        return None
        
def option_action(value):
    bookingList = []
    if (value == 1):
        print("View booking details")
        email = int(input("Please Input your booking email: "))
        print(f'bookingList: {bookingList}')
        for booking in bookingList:
            print(f'booking: {booking}')
            if email in booking:
                print('We go your eamil')
                print('This line does not work')
    elif(value == 2):
        print("Make a new booking")
        name = input("Input your booking name =>")
        email = input("Input your booking email =>")
        phone_number = input("Input your phone_number: ")
        note = input("Input your booking note =>")
        bookingList.append([name,email,phone_number,note])
    elif(value == 3):
            print("Delete a booking")
            removeID = int(input("Input your booking ID: "))
            for booking in bookingList:
                if(removeID in booking):
                    print(removeID)
                else:
                    print("We can not find it")
    elif(value == 4):
        print("Quit the application successfully!")
        exit()