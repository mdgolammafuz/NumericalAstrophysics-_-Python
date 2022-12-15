# Writing a Class ( here for instance Rectangle Class) in Python

class Rectangle:

    # Consctructor Method to Instantiate Objects using Rectangle Class
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color

    # calculate_area method to calculate the the areea of Objects created using Rectangle Class
    def calculate_area(self):
        return self.width * self.width


# Instanciation of Reactangle class to create rect object
rect = Rectangle(5, 3)

# type: ignore # Second Instance of Rectangle Class
rect1 = Rectangle(4, 2, "blue")
rect2 = Rectangle(3, 1, color="pink")  # Third Instance of Rectangle Class

print("Initial object : ", rect)
print("initial length attribute of the object : ", rect.length)
area = rect.calculate_area()
print("Area of the initial object : ", area)
