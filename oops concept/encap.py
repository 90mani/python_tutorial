class Students:
   def __init__(self, name, rank, points):
      self.name = name
      self.rank = rank
      self.points = points

   # custom function
   def demofunc(self):
      print("I am "+self.name)
      print("I got Rank ",+self.rank)
      

st1 = Students("chris", 1, 100)
st2 = Students("jeevi", 2, 90)
st3 = Students("kayal", 3, 76)


st1.demofunc()
st2.demofunc()
st3.demofunc()
