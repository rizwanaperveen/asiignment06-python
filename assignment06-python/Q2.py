#2. Using cls
#Assignment:
#Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def display(cls):
    
        print(f"Number of objects created: {cls.count}")
    
    @classmethod
    def reset(cls):
        cls.count = 0
Counter.display()
counter1 = Counter()
counter2 = Counter()
counter3 = Counter()
counter4 = Counter()
Counter.display()
Counter.reset()
#after reset it is zero
Counter.display()