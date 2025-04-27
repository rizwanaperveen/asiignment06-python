#6. Constructors and Destructors
#Assignment:
#Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self, message):
        print(f"{message}:Object created")

    def __del__(self):
        print("Object destroyed")


logger1 = Logger("Logger 1")
logger2 = Logger("Logger 2")
del logger1
del logger2