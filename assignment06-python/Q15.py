#15. Method Resolution Order (MRO) and Diamond Inheritance
#Assignment:
#Create four classes:

#A with a method show(),

#B and C that inherit from A and override show(),

#D that inherits from both B and C.

#Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("This is Class A")

class B(A):
    def show(A):
        print("This is Class B")

class C(A):
    def show(A):
        print("This is Class C")

class D(B, C):
    def show(self):
        print("This is Class D")

d = D()
d.show()