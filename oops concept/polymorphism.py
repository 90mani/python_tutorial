class India():
    def capital(self):
        print("New Delhi is the capital of India.")
 
    def people(self):
        print("Indian people are good people.")
 
 
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def people(self):
        print("USA people are very bad people.")
 
 
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.people()
    
