class Sprite:  # parent class

    def __init__(self, image):

        self.image = image

    def render(self):

        pass


class MovingSprite(Sprite):  # child class

    def __init__(self, image, speed):

        self.speed = speed
        super().__init__(image)

    def move(self):

        pass


"""
In this example, MovingSprite is a subclass of Sprite, which moves an image
rather than just rendering it in one place. All of the setup for the image
and rendering part of the Sprite is done in the Sprite’s constructor, so 
MovingSprite calls the constructor after it’s done handling the speed 
parameter.

Couldn’t we just set  this.image = image in MovingSprite’s 
constructor instead?

We could, but that solution doesn’t scale. Imagine if Sprite’s constructor
did other operations to the image (like calculating its height and width)
or imagine if MovingSprite got subclassed even further.

The `super()` approach allows you to reuse code rather than copying it, and
ensures that functionality is grouped logically - two of the main benefits
of object-oriented programming!

"""
