
"""
Suppose you work for a wildlife conservation organization. 
You are working on creating a system to educate the general public
about different animals and get them more interested in conservation.

Create a Tiger class that inherits from the Cat classand has a new coat pattern attribute. 

Change the behavior of instances of the Tiger class to include this coat pattern fact when they're printed.

The steps are as follows:

Go to your main.py file.

Define the Tiger class that inherits from the Cat class. Override its initializer and add a coat_pattern attribute with the value "striped".

Override the __str__() method and modify it to include mention of the coat pattern.

At the bottom of the script we have initialized an instance of the Tiger class and called print on the instance, which should display facts about the tiger.

(OUTPUT):

The tiger weighs 310kg, has a lifespan of 26 years and can run at a maximum speed of 65kph. It also has a striped coat.

"""


class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed

    def vocalize(self):
        print("Chuff")

    def __str__(self):
        return f"The {type(self).__name__.lower()} "\
            f"weighs {self.mass_in_kg}kg,"\
            f" has a lifespan of {self.lifespan_in_years} years and "\
            f"can run at a maximum speed of {self.speed_in_kph}kph."


# Write your Tiger class here

class Tiger(Cat):

    def __init__(self, mass, lifespan, speed, coat):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed
        self.coat_pattern = coat

    def __str__(self):
        return f"The {type(self).__name__.lower()} "\
            f"weighs {self.mass_in_kg}kg,"\
            f" has a lifespan of {self.lifespan_in_years} years and "\
            f"can run at a maximum speed of {self.speed_in_kph}kph."\
            f" It also has a {self.coat_pattern} coat"


"""
# This code is used to test your class

if __name__ == '__main__':
    tiger = Tiger(310, 26, 65)
    print(tiger)

class MovingSprite(Sprite):

    def __init__(self, image, speed):

        self.speed = speed
        super().__init__(image)

"""

tiger = Tiger(310, 2, 65, "striped")
print(tiger.__str__())
