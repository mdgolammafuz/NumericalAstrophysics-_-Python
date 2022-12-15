"""
In this activity, we'll define the Cat class from which we'll derive our other big cats. The class will have the methods vocalize and print_facts, and the attributes mass, lifespan, and speed.

The constructor method will take the arguments mass, lifespan, and speed from which it will add the attributes mass_in_kg, lifespan_in_years, and speed_in_kph to the object.

The vocalize method will print out Chuff, a non-threatening vocalization that's common to several big cats. The print_facts method will print out facts about the cat:

Define the Cat class:

class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed
 
    def vocalize(self):
        print("Chuff")
 
    def print_facts(self):
        print(f"The {type(self).__name__.lower()} "f"weighs {self.mass_in_kg}kg," f" has a lifespan of {self.lifespan_in_years} years and " f"can run at a maximum speed of {self.speed_in_kph}kph.")
The line type(self).__name__ means that we want the name of the current class of the object, in this case, Cat . We then call str.lower() on the name in our example.

Instantiate a cat instance and interact with the different methods and attributes it has:

In [1]: from main import Cat                                                                                                
 
In [2]: cat = Cat(4, 18, 48)                                                                                                
 
In [3]: cat.vocalize()                                                                                                      
Chuff
 
In [4]: cat.print_facts()                                                                                                   
The cat weighs 4kg, has a lifespan of 18 years and can run at a maximum speed of 48kph.
 
In [5]:
Create the subclasses Leopard, Cheetah, and Lion, which will inherit from the Cat class:

class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed
 
    def vocalize(self):
        print("Chuff")
 
    def print_facts(self):
        print(f"The {type(self).__name__.lower()} "f"weighs {self.mass_in_kg}kg," f" has a lifespan of {self.lifespan_in_years} years and " f"can run at a maximum speed of {self.speed_in_kph}kph.")
class Cheetah(Cat):
    pass
class Lion(Cat):
    pass
class Leopard(Cat):
    pass
Instantiate the new Leopard, Cheetah, and Lion classes.

Despite not adding any methods or attributes to these new classes, if we instantiate them, we'll need to pass in the same arguments that we do when instantiating the Cat class. The methods and attributes our instance will have will be identical to a Cat class instance:

Reimport your classes by starting the python interpreter in a new terminal or by restarting the existing python interpreter by entering quit().
"""


class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed

    def vocalize(self):
        print("Meowwww")

    def print_facts(self):
        print("The {} weighs {} kg, has a lifespan of {} years can run at a maximum speed of {} kph.".format(
            type(self).__name__.lower(), self.mass_in_kg, self.lifespan_in_years, self.speed_in_kph))


class Cheetah(Cat):
    # Overriding vocalize() method, Overriding is when a child class creates a new implementation of an inherited method.
    def vocalize(self):
        print("Chirrup")


class Lion(Cat):
    def vocalize(self):  # Overriding vocalize() method
        print("ROARRRRRRRR")


class Leopard(Cat):
    def vocalize(self):  # Overriding vocalize() method
        print("Roar")


cat = Cat(4, 18, 48)
cat.print_facts()
cat.vocalize()


cheetah = Cheetah(72, 12, 120)
cheetah.print_facts()
cheetah.vocalize()


leopard = Leopard(90, 17, 58)
leopard.print_facts()
leopard.vocalize()


lion = Lion(190, 14, 80)
lion.print_facts()
lion.vocalize()
