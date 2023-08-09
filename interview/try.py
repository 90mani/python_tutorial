def compress_string(input_str):
    compressed = ''
    count = 1


    for i in range(len(input_str)):
        if i < len(input_str) - 1 and input_str[i] == input_str[i+1]:
            count += 1
        else:
                compressed += input_str[i] + str(count)
                count = 1
    return compressed
input_str = "aaabbcaab"
compressed_output = compress_string(input_str)
print(compressed_output)
                
            
     
