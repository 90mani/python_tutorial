class student:
    def biodata(self,name,age,address,contact):
        self.name=name
        print("Name:",name)
        print("Age:",age)
        print("Address:",address)
        print("Contact:",contact)

    def data(self):
        print("Welcome:",self.name)

obj=student()
obj.biodata("Kayal",25,"Trichy",9988123470)
obj.data()
