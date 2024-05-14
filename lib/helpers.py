import os
from sqlalchemy  import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User

db_url = "sqlite:///yummy_sweet.db"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

bookingList = []

def clear_screen():
    clearscreen = lambda: os.system('clear')
    clearscreen()

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
    
def user_request():
    selected_value = prompt_input()

    while(not selected_value):
        selected_value = prompt_input()

    option_action(selected_value)

def option_action(value):
    clear_screen()
    if (value == 1):
        view_booking()
    elif(value == 2):
        add_new_booking()
    elif(value == 3):
        delete_booking()
    elif(value == 4):
        print("Quit the application successfully!")
        exit()


def view_booking():
    print("View booking details")
    email = input("Please Input your booking email: ")
    print(f'bookingList: {bookingList}')
    for booking in bookingList:
        print(f'booking: {booking}')
        if email in booking:
            print('We go your eamil')

    user_request()

def add_new_booking():
    print("Make a new booking")
    name = input("Input your booking name =>")
    email = input("Input your booking email =>")
    phone_number = input("Input your phone_number: ")
    note = input("Input your booking note =>")
    bookingList.append([name,email,phone_number,note])

    user_request()

def delete_booking():
    print("Delete a booking")
    removeID = int(input("Input your booking ID: "))
    for booking in bookingList:
        if(removeID in booking):
            print(removeID)
        else:
            print("We can not find it")
    
    user_request()

