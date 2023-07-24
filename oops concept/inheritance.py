class addition:
    def add(self):
        a = int(input("Enter the A value:"))
        b = int(input("Enter the B value:"))
        c = a + b
        print("Addition:",c)

class subtraction:
    def sub(self):
        a = int(input("Enter the A value:"))
        b = int(input("Enter the B value:"))
        c = a - b
        print("Subtraction:",c)

class Input(addition,subtraction):
    def base(self):
        self.add()
        self.sub()

obj=Input()
obj.base()

        
