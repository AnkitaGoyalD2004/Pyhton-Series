# Basic class and Object
# Create a car class with attributes like brand and model. Then create an instance of this class.

class Car:
    brand = None
    model = None

my_car = Car("Toyota", "Corolla")
print(my_car) # i will get an error of TypeError: Car() takes no arguments

#Why ? 

#Python automatically provides a default constructor when you don't define one, but that constructor doesn't accept arbitrary positional arguments.

# when we write Car("Toyota" , "Corolla") we're passing two arguments, but our class hasn't defined how to receive them. We need to use __init__() to initialize the object with those values.

class Cars:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

my_car = Cars("Toyota" , "Corolla")
print(my_car.brand , my_car.model) # output : Toyota Corolla
