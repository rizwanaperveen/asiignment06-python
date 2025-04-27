#13. Composition
#Assignment:
#Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.
# Define the Engine class

class Engine:
    def __init__(self, horsepower):
        
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} HP is starting."

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine
    
    def start_car(self):
        return f"{self.brand} car: {self.engine.start()}"


engine = Engine(500)
car = Car("Tesla", engine)

print(car.start_car())