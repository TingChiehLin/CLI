from helpers import intro, user_request, menu_action


def main():
    intro()
    choice = user_request(2)
    menu_action(choice)


if __name__ == "__main__":
    main()
