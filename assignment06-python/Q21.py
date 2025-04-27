#21. Make a Custom Class Iterable
#Assignment:
#Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object #iterable in a for-loop, counting down to 0.

import time

class Countdown:
    def __init__(self, start, delay=1):
        self.current = start
        self.delay = delay

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration

        else:
            number = self.current
            time.sleep(self.delay)
            self.current -= 2
            return number
    #Example
for num in Countdown(10, delay=2):
    print(num)