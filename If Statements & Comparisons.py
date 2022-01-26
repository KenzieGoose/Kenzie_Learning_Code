num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
num3 = input("Enter a number: ")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(num1, num2, num3))