#Create an Electric car class that inherits from the Car class and has an additional attribute battery_size

class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self , brand , model , battery_size):
        self.battery_size = battery_size
        super().__init__(brand , model) #super keyword is used for getting an acess of our exitasnce class


my_tesla = ElectricCar("Tesla" , "Model S" , "85kWh")
print(my_tesla.model)
print(my_tesla.full_name())
print(my_tesla.brand)
print(my_tesla.battery_size)

#output:
# Model S
# Tesla Model S
# Tesla
# 85kWh
 
