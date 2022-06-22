def arithmetic(num1,num2):
    if num1*num2 <= 1000:
        return num1*num2
    return num1+num2
num1 = int(input("Enter the value of a number:"))
num2 = int(input("enter the value of a number:"))

print(arithmetic(num1,num2))