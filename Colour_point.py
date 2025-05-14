from point import Point
import random

class ColourPoint(Point):
    def __init__(self, x, y, colour):
        """
        Init method:
        - Creates a ColourPoint object from x, y coords and a colour string.
        - Inherits x and y via super() from the Point class.
        - Raises TypeError if x or y are not numeric types.
        """
        if not isinstance(x, (int, float)): # x, tuple; isinstance asks what is the type of x
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")

        super().__init__(x, y) # access parent class through super() (do not have to write self.x & self.y again); replaces self.x & self.y
        self.colour = colour # edit __init__ & everything else carries over from Point

    def __str__(self):
        """
        Dunder method (__str__):
        - Defines how object prints when passed to print().
        - Returns colour + coords in string format.
        """
        return f"<{self.colour}: {self.x}, {self.y}>"

if __name__ == "__main__":
    p = ColourPoint(1, 2, "red")

    print(p.distance_to_orig()) # inherited method
    print(p)
