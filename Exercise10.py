first_list = [10,20,25,30,35, 27]
second_list = [40,45,60,75,90]
general_list2 = []
for num in range(len(first_list)):
    if(first_list[num]%2 == 0 ):
        general_list2.append(first_list[num])
    
for num in range(len(second_list)):
    if(second_list[num] % 2 != 0):
        general_list2.append(second_list[num])
    
print(general_list2)