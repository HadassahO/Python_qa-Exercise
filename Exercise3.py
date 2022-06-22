def PrintEvenCharacters(my_string):
    for index in range(len(my_string)):
        if(index % 2 == 0):
            output = my_string[index]
            print(f'\'{output}\',', end='')
            

check = "pynative"

PrintEvenCharacters(check)