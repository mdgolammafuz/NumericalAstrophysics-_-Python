from random import choice
import matplotlib.pyplot as plt 

class RandomWalk:

    """A class for generating random walks"""

    def __init__(self, number_of_steps = 500):

        # initialize the number of steps in he walk
        self.number_of_steps = number_of_steps

        # initial cooridinates of the step (x,y) = (0,0)
        self.x_coordinates = [0]
        self.y_coordinates = [0]


    def filling_the_walk(self) :

        # calculate all the coordinates of the walk 

        """continue taking steps until it reaches the
        total number_of_steps"""

        while len(self.x_coordinates) < self.number_of_steps :

            # taking a step in x-direction 
            x_direction = choice([-1,1])
            x_length = choice([0,1,2,3,4])
            x_step = x_direction*x_length

            # taking a step in y-direction
            y_direction = choice([-1,1])
            y_length = choice([0,1,2,3,4])
            y_step = y_direction*y_length

            # rejecting moves that goes nowhere
            if x_step == 0 and y_step == 0 :
                continue

            # the subsequent step
            x_next = self.x_coordinates[-1] + x_step
            y_next = self.y_coordinates[-1] + y_step
            self.x_coordinates.append(x_next)
            self.y_coordinates.append(y_next)


# Keep making new walks, as long as the program is active

while True:

    # Make a random walk 
    rw = RandomWalk()
    rw.filling_the_walk()
    
    plt.figure(dpi=128, figsize=(10,6))
    
    # plot the points
    # points = list(range(rw.x_coordinates))
    plt.scatter(rw.x_coordinates, rw.y_coordinates, edgecolor='none', s=1)
    
    # Emphasize the initial and final steps
    plt.scatter(0, 0, c = "green", edgecolors='none', s=4)
    plt.scatter(rw.x_coordinates[-1], rw.y_coordinates[-1], \
                 c= "red", edgecolors='none', s=4)
    
    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ") 
    if keep_running == 'n' :
        break
