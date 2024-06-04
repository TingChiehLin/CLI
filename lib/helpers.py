import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Restaurant, User, Booking

db_url = "sqlite:////Users/JayLinXR/Desktop/python-p3-cli-project-template/lib/db/yummy_sweet.db"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()


def clear_screen():
    os.system("clear")


def intro():
    print(
        "============================================================================"
    )
    print("Hello There! Welcome to Yummy Sweet Restaurant CLI App")
    print("Developed by Jay Lin")
    print(
        "============================================================================"
    )


def menu_option():
    print("Please choose what you want to do")
    print("Input 1 - View booking details")
    print("Input 2 - Quit")


def submenu_option():
    print("Input 1 - Make a new booking")
    print("Input 2 - Update a booking")
    print("Input 3 - Delete a booking")
    print("Input 4 - Quit")


def prompt_input(options):
    if options == 2:
        menu_option()
    elif options == 4:
        submenu_option()

    choice = int(input("Please Enter your choice: "))
    if choice <= options:
        return choice
    else:
        print("Please input correct range number")
        return None


def user_request(options):
    selected_value = prompt_input(options)

    while not selected_value:
        selected_value = prompt_input(options)
    if selected_value:
        return selected_value


def menu_action(value):
    clear_screen()
    if value == 1:
        view_booking()
    elif value == 2:
        print("Quit the application successfully!")
        exit()


def submenu_action(value):
    clear_screen()
    if value == 1:
        add_new_booking()
    elif value == 2:
        update_booking()
    elif value == 3:
        delete_booking()


def prompt_restaurant():
    print("Which restaurants do you like to book?")
    restaurants = session.query(Restaurant).all()

    for index, restaurant in enumerate(restaurants):
        print(f"${index} - ${restaurant.name}")

    choice = int(input("Please Enter your restaurant choice: "))
    if choice <= restaurant.count:
        return choice
    else:
        print(f"Please input correct range number from 0 to {restaurant.count}")
        return None


def prompt_email():
    email = input("Please Input your booking email: ")
    return email


def email_not_exist(email):
    print(f"Sorry, the {email} does not exist")
    print("Do you wish to input another email?")


def view_booking():
    clear_screen()
    email = prompt_email()

    user = session.query(User).filter(User.email == email).first()

    if user:
        print(f"User Name: {user.name}")
        for index, booking in enumerate(user.bookings):
            print(f"=========== {index+1} ===========")
            print(f"Booking Date: {booking.date}")
            print(f"Booking Time: {booking.time}")
            print(f"Booking Restaurant: {booking.restaurant.name}")
            print("=================================")
            choice = user_request(4)
            submenu_action(choice)
    else:
        email_not_exist(email)
        choice = int(
            input("Input 1 to attempt your email again, Input 2 go back to home page")
        )
        if choice == 1:
            view_booking()
        elif choice == 2:
            user_request(2)


def add_new_booking():
    restaurant_choice = prompt_restaurant()
    while not restaurant_choice:
        restaurant_choice = prompt_restaurant()

    # user = session
    # initial user data
    name = input("Input your booking name =>")
    email = input("Input your booking email =>")
    phone_number = input("Input your phone_number: ")
    note = input("Input your booking note =>")
    new_user = User(name, email, phone_number, note)

    time = input("Input your booking time=>")
    date = input("Input your booking date=?")
    new_booking = Booking()

    session.add(new_user)
    session.commit()
    user_request(4)


def update_booking():
    email = input("Please Input your booking email=> ")
    user = session.query(User).filter(User.email == email).first()
    for index, booking in enumerate(user.bookings):
        print(f"Input your {index} number to update your {booking}")
        choice = int(input("Please Enter your choice: "))
        if index == choice:
            updateDate = input("Input your update date")
            booking.date = updateDate
            session.commit()
        else:
            print("Sorry We can not find your bookings")
            update_booking()
    user_request(4)


def delete_booking():
    clear_screen()
    email = prompt_email()
    user = session.query(User).filter(User.email == email).first()

    if user:
        for index, booking in enumerate(user.bookinbgs):
            print(
                f"Input your {index} number to update your ${booking.restaurant.name}, Booking Time: ${booking.time}"
            )
            choice = int(input("Please Enter your choice: "))
            if index == choice:
                session.delete(booking)
                session.commit()
        user_request(4)
    else:
        email_not_exist(email)
        choice = int(
            input("Input 1 to attempt your email again, Input 2 go back to home page")
        )
        if choice == 1:
            delete_booking()
        elif choice == 2:
            user_request(2)
