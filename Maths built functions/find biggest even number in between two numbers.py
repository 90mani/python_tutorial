#find biggest even number in between two numbers

def test(m,n):
    if m > n or (m==n and m%2==1):
        return -1
    return n if n %2 ==0 else n-1

m=int(input("enter number1:"))
n=int(input("enter number2:"))

print("biggest even number between",m,"and",n)
print(test(m,n))