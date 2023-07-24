# single inheritance
class father():#base class
    f_name= "jeeva"
    f_age= 50

class son(father):#child class
    s_name= "thomas"
    s_age= 30

obj=son()
print("father name is",obj.f_name)
print("son name is",obj.s_name)






#Multilevei inheritance    
class gfather():#base class
    gf_name= "raja"
    gf_age= 50

class father(gfather):#child class
    f_name= "david"
    f_age= 30
class son(father):
    s_name="ajay"
    s_age= 10

obj=son()
print("gfather name is",obj.gf_name)
print("father name is",obj.f_name)
print("son name is",obj.s_name)



#Multiple inheritance
class father():#base class
    f_name= "dhanush"
    f_age= 50

class mother():#base class
    m_name= "rani"
    m_age= 30
class son(father,mother):#child class
    s_name= "ajay"
    s_age= 10

obj=son()
print("father name is",obj.f_name)
print("mother name is",obj.m_name)
print("son name is",obj.s_name)



