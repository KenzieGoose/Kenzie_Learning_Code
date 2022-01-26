from Student import Student

user_num = input("Enter Student ID number: ")

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Tim", "MBA", 2.7, False)


def translate(lookup):
    translation = ""
    for letter in lookup:
        if letter.lower() in "n":
            if letter.isupper():
                translation = translation + "n"
            else:
                translation = translation + "n"
        else:
            translation = translation + letter
    return translation


user_lookup = translate(input("Enter Name, Major, GPA, Probation: "))

# def students():
#    if students == ('student' + user_num + "." + user_lookup):
#        students == students("student" + user_num + '.' + user_lookup)
#    return students()

students = str('student{0}.{1}'.format(user_num, user_lookup))

print(students)
print(student1.name)
