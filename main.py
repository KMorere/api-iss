from business import get_iss_position, get_astronaut_data

def main():
    choice = get_choice()

    if choice == "1":
        print(get_iss_position())
        get_choice()

    elif choice == "2":
        print(get_astronaut_data())
        get_choice()

    elif choice == "0":
        print("Leaving...")
    else:
        print("Unvalid choice, select a number between 0-2")
        get_choice()


def get_choice():
    print()
    print("=====ISS MENU=====")
    print("1 - Display ISS coordinates")
    print("2 - Display Astronauts information")
    print("0 - Leave")
    print()

    return input("Select a choice: ")


if __name__ == "__main__":
    main()