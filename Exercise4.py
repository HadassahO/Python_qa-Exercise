def RemoveString(user_string, count):
    str = ''
    if(n > len(user_string)): return
    
    for index in range(len(user_string)):
        if(index <= count): continue
        
        str+=user_string[index]
        
    return str

_input = "Live it love it"

n = 2

result = RemoveString(_input,n)
print(result)
