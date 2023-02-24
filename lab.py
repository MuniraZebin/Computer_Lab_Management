import json


class Lab:
    def __init__(self):
        self.pc_number = 0
        self.os = ""
        self.status = ""

    def display_pcs(self):
        with open("./Lab.json") as file_obj:
            pcs = json.load(file_obj)

        if len(pcs) > 0:
            for i in pcs:
                print("\nPC number:", i['pc_id'])
                print("Operating System:", i['pc_os'])
                print("Current status:", i['pc_status'])

            choice = input("\nWant to search any PC to display?(y/n): ")
            if choice == 'y' or choice == 'Y':
                self.search_pc()

        else:
            print("No PC registered yet")

    def add_pc(self):
        valid = True
        with open("./Lab.json") as file_obj:
            pcs = json.load(file_obj)
        try:
            while True:
                self.pc_number = int(input("Enter PC number: "))
                for i in pcs:
                    if i['pc_id'] == self.pc_number:
                        print("PC already exist!\n")
                        valid = False
                        break

                if valid:
                    break
                else:
                    valid = True

            self.os = input("Enter Operating System: ")
            self.status = input("Enter current status: ")
        except:
            print("Invalid Input!\n")
            self.add_pc()

        pcs.append({
            "pc_id": self.pc_number,
            "pc_os": self.os,
            "pc_status": self.status
        })

        with open(f"./Lab.json", "w") as file:
            json.dump(pcs, file)

        print("PC has been added!")

    def update_pc(self):
        valid = False
        with open("./Lab.json") as file_obj:
            pcs = json.load(file_obj)
        try:
            while True:
                if self.pc_number == 0:
                    self.pc_number = int(input("Enter PC number you want to update information: "))

                for i in pcs:
                    if i['pc_id'] == self.pc_number:
                        choice = 0
                        while 1 > choice or choice > 2:
                            choice = int(input("Which info you want to update?\n"
                                               "1. Operating System. \n"
                                               "2. PC current status.\n\n"
                                               "Enter: "))
                        if choice == 1:
                            self.os = input("Enter Operating System: ")
                            i['pc_os'] = self.os
                            with open("./Lab.json", "w") as file_update:
                                json.dump(pcs, file_update)

                        elif choice == 2:
                            self.status = input("Enter current status: ")
                            i['pc_status'] = self.status
                            with open("./Lab.json", "w") as file_update:
                                json.dump(pcs, file_update)
                        valid = True
                        break

                if valid:
                    break
                else:
                    print("PC does not exist!\n")
                    valid = False
        except:
            print("Invalid Input!\n")
            self.update_pc()

        print("Information updated!")

    def remove_pc(self):
        valid = False
        with open("./Lab.json") as file_obj:
            pcs = json.load(file_obj)

        while True:
            self.pc_number = int(input("Enter PC number you want to remove: "))
            for num, i in enumerate(pcs):
                if i['pc_id'] == self.pc_number:
                    pcs.pop(num)
                    valid = True
                    break

            if valid:
                break
            else:
                print("PC does not exist!\n")
                valid = False

        with open("./Lab.json", "w") as file_update:
            json.dump(pcs, file_update)

        print("PC has been removed!")

    def search_pc(self):
        valid = False
        with open("./Lab.json") as file_obj:
            pcs = json.load(file_obj)

        while True:
            self.pc_number = int(input("Enter PC number you want to search: "))
            for i in pcs:
                if i['pc_id'] == self.pc_number:
                    print("\nPC number:", i['pc_id'])
                    print("Operating System:", i['pc_os'])
                    print("Current status:", i['pc_status'])
                    choice = input("\nWant to update this PC information?(y/n): ")
                    if choice == 'y' or choice == 'Y':
                        self.update_pc()

                    valid = True
                    break

            if valid:
                break
            else:
                print("PC does not exist!\n")
                valid = False
