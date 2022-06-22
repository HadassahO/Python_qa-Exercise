def CheckNumber(numberlist):
    if numberlist[0]==numberlist[-1]:
        return True
    return False
    
numberlist = [10,20,30,40,10]
new_list =[75,65,35,75,30]
result = CheckNumber(numberlist)
result2 = CheckNumber(new_list)
print(result)
print(result2)
