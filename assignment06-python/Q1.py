#1. Using self
#Assignment:
#Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    #A function that print student details
    def display(self):
        print("Student Detail:")
        print(f"Student Name:{self.name}, \nMarks:{self.marks}")

student = Student("Ali",100)
student.display()