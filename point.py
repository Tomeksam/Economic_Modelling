
import random

class Point: # make a type of object
    def __init__(self, x, y):
        """
        Initialize a Point object.
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x # inside the point, x and y are its attributes
        self.y = y # and assign the value x to it

    def __str__(self):
        """
        Magic Method that
        :param self:
        :return: Point (x,y)
        """

        return f"Point ({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

    def distance_orig(self):
        return (self.x**2 + self.y**2)**0.5 # pythagoras, square root of the sum of x and y squared

    def __gt__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_org()
        return my_distance == other_distance

if __name__ == "__main__": # importing protection to others, only run if in this file
    # instantiate
    p = Point(1, 2) # p is an instance of 1 and 2
    p2 = Point(2, 3)
    p4 = Point(4.4, -55)
    print(f"p.x={p.x} and p.y={p.y}")

    p.x = 20
    print(f"p.x={p.x} and p.y={p.y}")
    print(p)
    # Create a list of 5 random points
    points = []
    for i in range(5):
        points.append(Point(random.randint(-10, 10), # x value
                            random.randint(-10, 10))) # y value
    print("I got these 5 random points:")
    for p in points: #points is a list
        print(p)

    print(points)
    p = Point(3,4)
    print(p.distance_orig())
    p2 = Point(1,1)
    print(f"i am comparing p > p2: {p>p2}")
    print("the sorted list of points is:")
    points.sort()
    print(points)


#if we want to print then we use rpr