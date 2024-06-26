import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Restaurant, User, Booking

db_url = "sqlite:////Users/JayLinXR/Desktop/python-p3-cli-project-template/lib/db/yummy_sweet.db"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

user = None


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
    print("What will you do next?")
    selected_value = prompt_input(options)

    while not selected_value:
        selected_value = prompt_input(options)
    if selected_value:
        return selected_value


def menu_action(user_choice):
    clear_screen()
    if user_choice == 1:
        view_booking()
    elif user_choice == 2:
        print("Quit the application successfully!")
        exit()


def submenu_action(selected_user, user_choice, user_bookings):
    if user_choice == 1:
        add_new_booking(selected_user)
    elif user_choice == 2:
        update_booking(user_bookings)
    elif user_choice == 3:
        delete_booking(user_bookings)
    elif user_choice == 4:
        exit()


def prompt_restaurant():
    print("Which restaurants do you like to book?")
    restaurants = session.query(Restaurant).all()

    for index, restaurant in enumerate(restaurants):
        print(f"{index+1} - {restaurant.name}, Rating: {restaurant.rate}")

    user_Input = int(input("Please Enter your restaurant choice: "))
    if user_Input <= len(restaurants):
        selected_restaurant = restaurants[user_Input - 1]
        print(f"selected_restaurant {selected_restaurant}")
        return selected_restaurant
    else:
        print(f"Please input correct range number from 1 to {len(restaurants)-1}")
        return None


def prompt_email():
    email = input("Please Input your email: ")
    return email


def email_not_exist(email):
    print(f"Sorry, the {email} does not exist")
    print("Do you wish to input another email?")


def check_member():
    user_member = int(
        input("Are you our member? Yes => Please Input 1, No => Please Input 2: ")
    )
    if user_member == 1:
        global user
        user_email = prompt_email()
        user = session.query(User).filter(User.email == user_email).first()
        while not user:
            print("Sorry we can not find your user, please input right e-mail again")
            user_email = prompt_email()
            user = session.query(User).filter(User.email == user_email).first()
        print(f"Welcome {user.name}: ")
        return True

    elif user_member == 2:
        print(
            "You have not registed our member, Please registed a new member by e-mail"
        )
        return False
    else:
        print("Please Input right range from 1 to 2")
        check_member()


def show_booking():
    for index, booking in enumerate(user.bookings):
        print(f"=========== No:{index+1} ===========")
        print(f"Booking User Name: {user.name}")
        print(f"Booking Date: {booking.date}")
        print(f"Booking Time: {booking.time}")
        print(f"Booking Restaurant: {booking.restaurant.name}")
        print("=================================")


def check_booking():
    if not user.bookings:
        print(
            f"Sorry {user.name}, we could not find any your bookings. Please create a booking"
        )
        print("Do you want to create a new booking?")
        user_Input = int(
            input("Input 1 to creat a new booking, Input 2 to exit the application => ")
        )
        if user_Input == 1:
            add_new_booking(user)
        elif user_Input == 2:
            exit()
    else:
        show_booking()
        user_Input = user_request(4)
        submenu_action(user, user_Input, user.bookings)


def create_new_user():
    print("=== Create a new user ===")
    name = input("Input your user name => ")
    email = input("Input your email => ")
    phone_number = input("Input your phone_number: ")
    note = input("Input your booking note => ")
    new_user = User(name, email, phone_number, note)
    session.add(new_user)
    session.commit()
    print("Create a new user sucessfully!")
    user_Input = user_request(2)
    menu_action(user_Input)


def view_booking():
    clear_screen()
    is_member = check_member()
    if is_member:
        check_booking()
    else:
        create_new_user()


def add_new_booking(selected_user):
    clear_screen()

    restaurant_choice = prompt_restaurant()
    while not restaurant_choice:
        restaurant_choice = prompt_restaurant()
    print(f"restaurant_choice -> {restaurant_choice}")
    time = input("Input your booking time=> ")
    date = input("Input your booking date=> ")
    new_booking = Booking(time, date)
    new_booking.restaurant = restaurant_choice
    new_booking.user = selected_user
    # new_booking.restaurant_id = restaurant_choice.id
    # new_booking.user_id = selected_user.id
    session.add(new_booking)
    session.commit()
    print("Create a new booking successfully")
    show_booking()
    user_Input = user_request(4)
    submenu_action(user, user_Input, user.bookings)


def update_booking(user_bookings):
    print("Input your booking number to update your booking")
    user_Input = int(input("Please Enter your choice: "))
    selected_booking = user_bookings[user_Input - 1]
    if selected_booking:
        print(f"Booking Number: {selected_booking.id}")
        print(f"Booking Time: {selected_booking.time}")
        print(f"Booking Date: {selected_booking.date}")
        print("======================================")
        choice = int(
            input("Are you sure that you want to update? 1 => YES, 2 => NO =>")
        )
        if choice == 1:
            update_date = input("Input your update date =>")
            selected_booking.date = update_date
            update_time = input("Input your update time =>")
            selected_booking.time = update_time
            session.commit()
            user_Input = user_request(4)
            submenu_action(user, user_Input, user.bookings)
        elif choice == 2:
            choice = int(
                input("Do you want to go back to options page? 1 => YES, 2 => NO =>")
            )
            if choice == 1:
                user_Input = user_request(4)
                submenu_action(user, user_Input, user.bookings)
            elif choice == 2:
                update_booking(user_bookings)
        else:
            print(f"Please input valid booking number, 1 to {len(user_bookings)}")
            update_booking(user_bookings)


def delete_booking(user_bookings):
    print("Input your booking number to delete your booking")
    user_Input = int(input("Please Enter your choice: "))
    selected_booking = user_bookings[user_Input - 1]
    if selected_booking:
        print(f"Booking Number: {selected_booking.id}")
        print(f"Booking Time: {selected_booking.time}")
        print(f"Booking Date: {selected_booking.date}")
        print("======================================")
        choice = int(
            input("Are you sure that you want to delete? 1 => YES, 2 => NO =>")
        )
        if choice == 1:
            session.delete(selected_booking)
            session.commit()
            user_Input = user_request(4)
            submenu_action(user, user_Input, user.bookings)
        elif choice == 2:
            choice = int(
                input("Do you want to go back to options page? 1 => YES, 2 => NO =>")
            )
            if choice == 1:
                user_Input = user_request(4)
                submenu_action(user, user_Input, user.bookings)
            elif choice == 2:
                delete_booking(user_bookings)
        else:
            print(f"Please input valid booking number, 1 to {len(user_bookings)}")
            delete_booking(user_bookings)
