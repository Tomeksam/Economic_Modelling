import random

from point import Point

class PointException(Exception):
    pass #when you are forced by the syntax to have some code, essentially skip

class ColourPoint(Point): #inheritence
    def __init__(self, x, y, colour):
        if not PointException(x, (int,float)):
            raise TypeError("x must be a number")
        if not PointException(y, (int, float)):
            raise TypeError("y must be a number")

        super().__init__(x,y) # this replaces the self.x and self.y, calls the class
        self.colour = colour

    def __str__(self):
        return f"<{self.colour}: {self.x}, {self.y}>"

p = ColourPoint(1,2,"balls") # we want to prevent someone hacking and inputting p= 7 for example
print(p.distance_orig())
print(p)
