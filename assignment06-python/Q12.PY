#12. Static Methods
#Assignment:
#Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
  @staticmethod
  def celsius_to_fahrenheit(c):
    return(c*9/5)+32

  @staticmethod
  def fahrenheit_to_celsius(f):
    return (f-32)*5/9

print(TemperatureConverter.celsius_to_fahrenheit(10))
print(TemperatureConverter.fahrenheit_to_celsius(50))

print(TemperatureConverter.celsius_to_fahrenheit(10))