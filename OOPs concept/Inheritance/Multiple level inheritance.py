#multiple level inheritance

class grandpa ():
    def phone(self):
        print("grandpa phone")

class dad (grandpa):
    def money(self):
        print("dads money")

class son (dad):
    def laptop(self):
        print("sons laptop")


saran=son()
saran.laptop()
saran.money()

d1=dad()
d1.phone()
d1.money