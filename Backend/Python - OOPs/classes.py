# Syntax:
# class ClassName:
#   variables or data members (attributes)
#   methods or functions (behavior)

# 100 students data with thier names, age, address, school, class/grade, section
class Student:
    # class method

    # constructor - It is a special method used to initialize the variables of the class. It is called Automatically whenever object is created for the class
    
    # Constructor has been called
    # def __init__(self):
    #     print("Constructor has been called")

    # default constructor - if we assign some default value to any of the variable, it is called as default constructor

    # paramterized constructor - the variables will be empty and value will be initialized during object creation

    def __init__(self, name, age, branch, semester, college="ParvaM"):
        self.name = name
        self.age = age
        self.college = college
        self.branch = branch 
        self.semester = semester

    def printDetails(self):
        print("Student Details will be displayed here:")
        print(f"Name of the student: {self.name}, he is {self.age} years old and studying in {self.college} in {self.branch} branch in {self.semester} semester")

# Initialization of an Object
# std1, std2 are the objects of Student Class
std1 = Student(name = "Akshay", age = 24, branch="Information Science", college="ABC College", semester=8)
std2 = Student(name = "Ajay", age = 23, branch="Computer Science", college="ParvaM College", semester=6)
std3 = Student(name = "Vijay", age = 25, branch="AIML", semester=8)

# self is going to refer the object of the class
Student.printDetails(std1)

# Both can be used for calling the methods
# std2.printDetails(std2)
std2.printDetails()
std3.printDetails()