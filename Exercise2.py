
from tabulate import tabulate
prev_no = 0
list =[]
for i in range(1,11):
    sum = prev_no + i
    temp = [i,sum]
    list.append(temp)
    prev_no = i 
    
col_names = ["previous number", "Current number"]
print(tabulate(list, headers=col_names, tablefmt='grid'))