

class Student:
    
     # protected data members
      name = None
      __roll = None
      _branch = None
    
     # constructor
      def _init_(self, name, roll, branch): 
          self.name = name
          self.__roll = roll
          self._branch = branch
      def __displayRollNumber(self):
          print(self.__roll)
    
      
class Geek(Student):
 
       # constructor
       def _init_(self, name, roll, branch):
                Student._init_(self, name, roll, branch)
         
        
# creating objects of the derived class       
obj = Geek("R2J", 1706256, "Information Technology")

print(obj.name)
obj.__displayRollNumber()
