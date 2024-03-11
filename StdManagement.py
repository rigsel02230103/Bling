students_list = []
students_dict = {}

name = input("Enter student's name: ")
age = input("Enter student's age: ")
grade = input("Enter student's grade: ")

students_list.append(name)
students_dict[name] = {"age": age, "grade": grade}
print("Student information added successfully!")

print("Student Details: ")
for name, info in students_dict.items():
    print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")

#To search
student_search = input("Enter the name of the student to search or simply enter to skip: ")
if name in students_dict:
    info = student[name]
    print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
else:
    print("Student not found!")

#To remove
student_remove = input("Enter the name of the student to remove or simply enter to skip")
if name in students_dict:
    student_list.remove(name)
    del students_dict[name]
    print("Student has been removed successfully")
else:
    print("Student not found")



