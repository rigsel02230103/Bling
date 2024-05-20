class Person:
    def __init__ (self, name, age, CID):
        self.name = name
        self.age = age
        self.CID = CID
    
    def walk(self):
        print(self.name,"walks")
    def talk(self):
        print(self.name,"talks")
    def eat(self):
        print(self.name,"eats")
    def sleep(self):
        print(self.name,"sleeps")

class Student(Person):
    def __init__ (self, name, age, CID, stdID, course, year, GPA):
        super().__init__(name, age, CID)
        self.stdID = stdID
        self.course = course
        self.year = year
        self.GPA = GPA

    def study(self):
        print(self.name,"Studies")
    def writes_exams(self):
        print(self.name,"Has examinations")
    def attend_class(self):
        print(self.name,"Has to go to class")

class Teacher(Person):
    def __init__ (self, name, age, CID, subject, salary, department, designation):
        super().__init__(name, age, CID)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(self.name,"Goes to teach")
    def grading(self):
        print(self.name,"Grades students")
    def meetings(self):
        print(self.name,"Goes to attend meeting")

nima = Student("nima", 14, 1209384, 2093842, "ECE", 1, 3.5)
Vincent = Teacher("Vincent", 34, 374435, "Mgt", "NU30000", "ECE", "Professor")
print(nima.name)
print(nima.course)
nima.eat()
nima.study()
print(Vincent.name)
print(Vincent.salary)
Vincent.sleep()
Vincent.grading()