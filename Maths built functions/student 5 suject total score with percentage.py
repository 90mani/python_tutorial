sub1 = int(input("tamil:"))
sub2 = int(input("english:"))
sub3 = int(input("maths:"))
sub4 = int(input("science:"))
sub5 = int(input("social science:"))

print()
total = sub1+sub2+sub3+sub4+sub5
print("total score:",total)
percentage = (total/500)*100
print("percentage=",percentage,"%")