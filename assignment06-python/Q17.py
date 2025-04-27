#17. Class Decorators
#Assignment:
#Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

# Define the decorator

def add_greeting(cls):
    def greet(self):
        return f"Hello {self.name} from Decorator!"
    
    cls.greet = greet
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Test
p = Person("Ali")
print(p.greet())  # Output: Hello from Decorator!
