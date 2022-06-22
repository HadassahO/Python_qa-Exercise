numbers = '121'
count = len(numbers) - 1
output = ''
while count >= 0:
    output += numbers[count]
    count-=1
    
if(output == numbers): 
    print(f'It is a palindrome:{output}')
