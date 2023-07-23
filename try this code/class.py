class Bird:
  def intro(self):
    pass
     
  def fly(self):
    pass
  
   
class sparrow(Bird):
 
  def fly(self):
    print("sparrow can fly")
   
     
class ostrich(Bird):
  def fly(self):
    print("Ostriches cannot fly.")   
     
 

obj_ost = ostrich()
obj_ost.fly();
obj_ost.intro();
