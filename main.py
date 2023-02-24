import json
from lab import Lab


def main():
    print("Name: Munira Zebin \nId: 19-41014-2 \nComputer Lab Management Application\n")
    while True:
        pc = Lab()
        print("\n1. Add a new PC")
        print("2. Update information of an existing PC")
        print("3. Remove an existing PC")
        print("4. Display all the PCs")
        print("5. Search for a particular PC")
        print("0. Quit")
        user_choice = input("\nEnter your choice: ")
        if user_choice == '1':
            pc.add_pc()

        elif user_choice == '2':
            pc.update_pc()

        elif user_choice == '3':
            pc.remove_pc()

        elif user_choice == '4':
            pc.display_pcs()

        elif user_choice == '5':
            pc.search_pc()

        elif user_choice == '0':
            print("Application Terminated!")
            break

        else:
            print("Entered wrong choice!\nTry again...")


if __name__ == '__main__':
    main()
