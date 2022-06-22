numbers = '7536'
count = len(numbers) - 1
output = ''
while count >= 0:
    output += numbers[count]+' '
    count-=1
print(f'\'{output}\'')