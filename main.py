import json
from lab import Lab


def main():
    print("Name: \nId: \nComputer Lab Management Application\n")

    while True:
        print("\n1. Add a new PC")
        print("2. Update information of an existing PC")
        print("3. Remove an existing PC")
        print("4. Display information about all the PCs")
        print("5. Display all information of a PC")
        print("6. Search for a particular PC and display the information")
        print("7. Store all the PC available in the application into a text file")
        print("8. Quit")
        user_choice = input("\nEnter your choice: ")
        if user_choice == '1':
            pc = Lab()
            pc.add_pc()

        elif user_choice == '8':
            print("Application Terminated!")
            break

        else:
            print("Entered wrong choice!\nTry again...")


if __name__ == '__main__':
    main()
