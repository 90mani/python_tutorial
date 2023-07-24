#multiple inheritance

class dad ():
    def phone(self):
        print("dads phone")

class mom ():
    def sweet(self):
        print("mom sweet")

class son (dad,mom):
    def laptop(self):
        print("sons laptop")


saran=son()
saran.phone()
saran.sweet()