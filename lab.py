import json


class Lab:
    def __init__(self):
        self.pc_number = 0
        self.os = ""
        self.status = ""

    def display_pc(self):
        pass

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

    def update_pc(self):
        valid = False
        with open("./Lab.json") as file_obj:
            pcs = json.load(file_obj)
        try:
            while True:
                self.pc_number = int(input("Enter PC number you want to update information: "))
                for i in pcs:
                    if i['pc_id'] == self.pc_number:
                        valid = True
                        break

                if valid:
                    break
                else:
                    print("PC does not exist!\n")
                    valid = False

            choice = 0
            while 1 > choice or choice > 2:
                choice = int(input("Which info you want to update?\n"
                                   "1. Operating System. \n"
                                   "2. PC current status.\n\n"
                                   "Enter: "))

            for i in pcs:
                if i['pc_id'] == self.pc_number:
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
        except:
            print("Invalid Input!\n")
            self.update_pc()

    def remove_pc(self):
        valid = False
        with open("./Lab.json") as file_obj:
            pcs = json.load(file_obj)

        while True:
            self.pc_number = int(input("Enter PC number you want to update information: "))
            for i in pcs:
                if i['pc_id'] == self.pc_number:
                    valid = True
                    break

            if valid:
                break
            else:
                print("PC does not exist!\n")
                valid = False

        with open("./Lab.json") as file:
            data = json.load(file)

        for num, i in enumerate(data):
            if i['pc_id'] == self.pc_number:
                data.pop(num)
                break

        with open("./Lab.json", "w") as file_update:
            json.dump(data, file_update)

    def search_pc(self):
        pass
