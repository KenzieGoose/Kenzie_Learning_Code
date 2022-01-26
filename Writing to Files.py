


employee_file = open("employees.txt", "a")

employee_file.write("\n")
employee_file.write(input("Enter name and position: "))

employee_file.close()