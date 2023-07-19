def manual_tokens_generation(token_count):
    token_list=[]
    for i in range(token_count):
        token_list.append(i)
        return token_list
    

result = manual_tokens_generation (10)
print(result)


def generator_function(token_count):
    for i in range(token_count):
        yield i

result_gen=generator_function(10)
print(result_gen)


for i in result_gen:
    print(i)

 
