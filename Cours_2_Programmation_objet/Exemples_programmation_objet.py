############# from PYTHON CRASH COURSE (Eric Matthes)

##############Creating a dog Class

class Dog:
    """ A simple attempt to model a dog"""
    def __init__(self,name,age):
        """ initialise name and age attributes """
        self.name=name
        self.age=age
    def sit(self):
        """ simulate a dog sitting in response to command"""
        print(f"{self.name} is now sitting")
    def roll_over(self):
        """ simulate rolling over in response to command"""
        print(f"{self.name} rolled over !")
        
#my_dog=Dog("Willie",5)
#print(f"My dog's name is {my_dog.name}")
#print(f"My dog is {my_dog.age} years old")
#
#my_dog.sit()
#my_dog.roll_over()
#
#your_dog=Dog("Lucie",3)
#
#print(f"\nMy dog's name is {your_dog.name}")
#print(f"My dog is {your_dog.age} years old")
#
#your_dog.sit()
#your_dog.roll_over()

##########creation a Car class

class Car:
    """ A simple attempt to represent a car"""
    def __init__(self,make,model,year):
        """ Initialize attributes to describe a car"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name"""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car s mileage"""
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back
        """
        if  mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer !")
    def incremente_odometer(self,miles):
        """
        Add the given amount to the odometer reading
        """
        self.odometer_reading+=miles
        
#my_new_car=Car('audi','a4',2024)
#print(my_new_car.get_descriptive_name())
#my_new_car.read_odometer()
#
#my_new_car.odometer_reading=23
#my_new_car.read_odometer()
#
#my_new_car.update_odometer(10)
#my_new_car.read_odometer()
#
#my_used_car=Car('Subaru','ouback',2019)
#print(my_used_car.get_descriptive_name())
#
#my_used_car.update_odometer(23_500)
#my_used_car.read_odometer()
#
#my_used_car.incremente_odometer(100)
#my_used_car.read_odometer()
#

#class Electriccar(Car):
#    """
#    Represent aspects of a car, specific to electric vehicles
#    """
#    def __init__(self,make,model,year):
#        """
#        Initialize attribute of the parent class
#        Then initialize attributes specific to an electric car
#        """
#        super().__init__(make,model,year)
#        self.battery_size=40
#        
#    def describe_battery(self):
#        """
#        Print a statement describing the battery size
#        """
#        print(f"This car has a {self.battery_size}-kWh battery")
#        
#my_leaf=Electriccar('Nissan','leaf',2024)
#print(my_leaf.get_descriptive_name())
#my_leaf.describe_battery()


class Battery:
    """
    A simple attempt to model a battery from an electric car
    """
    def __init__(self,battery_size=40):
        self.battery_size=battery_size
    def describe_battery(self):
        """
        Print a statement describing the battery size
        """
        print(f"This car has a {self.battery_size}-kWh battery")
        
    def get_range(self):
        """
        Print a statement about the range this battery provides
        """
        if self.battery_size==40:
            range=150
        elif self.battery_size==65:
            range=225
        print(f'This car can go about {range} miles on full charge')
        
class Electriccar(Car):
    """
    Represent aspects of a car, specific to electric vehicles
    """
    def __init__(self,make,model,year):
        """
        Initialize attribute of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make,model,year)
        self.battery=Battery()
        
        
my_leaf=Electriccar('Nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

