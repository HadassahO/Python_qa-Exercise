def divisiblebyfive(numbers):
    for index in range(len(numbers)):
        if numbers[index] % 5 == 0:
            print(numbers[index])
            
new_list = [3,2,5,16,25,81,75]
divisiblebyfive(new_list)