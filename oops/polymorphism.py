#function overloading
class Demo():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            c=a+b+c
        elif a!=None and b!=None:
            c=a+b
        else:
             c=a
        print(c)
obj= Demo()
obj.sum(10,20,30)




#function overriding
class Demo():
    def fun(self):
        print("Demo class")
class Demo1(Demo):
    def fun(self):
        print('Demo1 class')
obj = Demo1()
obj.fun()
    

            
