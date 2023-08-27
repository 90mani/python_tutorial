# generator expression
generator_exp = (i * 5 for i in range(5) if i%2==0)
 
for i in generator_exp:
    print(i)
