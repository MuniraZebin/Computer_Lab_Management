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
        pass

    def remove_pc(self):
        pass

    def search_pc(self):
        pass


