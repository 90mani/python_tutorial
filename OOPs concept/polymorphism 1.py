#polymorphism




class employee:
  def company(self):
    print("There are many employee in our company.")
     
  def id(self):
    print("Most of the have no specific company id.")
   
class bala (employee):
  def init(self):
    print("test")
  def id(self):
    print("bala have an employee id")
  def bala(self):
    print("It's bala")
     
class saran(bala):
  def fly(self):
    print("saran have no employee id.")   
     
 

obj_saran = saran()
obj_saran.bala();
obj_saran.company();