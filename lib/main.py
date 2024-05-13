import sys
from helpers import main_menu,prompt_input, menu_option,  option_action

def main():
    main_menu()
    selected_value = prompt_input()

    while(not selected_value):
        selected_value = prompt_input()

    option_action(selected_value)
    main()

if __name__ == "__main__":
    main()