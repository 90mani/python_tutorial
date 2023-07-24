#inheritance

class dad ():
    def phone(self):
        print("dads phone")

class son (dad):
    def laptop(self):
        print("sons laptop")


saran=son()
saran.phone()