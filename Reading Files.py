

employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)


employees_file.close()