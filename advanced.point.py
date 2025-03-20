from colour_point2 import ColourPoint, PointException
# this is demonstrating the factory method as we return a new instance of the class

class AdvancedPoint(ColourPoint): # lets define a lsit of acceptable colours
    COLOURS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"] # not a attribute per instance, its the same for each class
    def __init__(self, x, y, colour):
        if colour not in self.COLOURS:
            raise PointException(f"Invalid colour bro must be one of the ones i{self.COLOURS}")
        self._x = x
        self._y = y
        self._colour = colour

    @property # allows for function without the brackts? with a hidden value of x, method that doesnt take any other parameters
    def x(self):
        return self._x # getter method

    @property  # allows for function without the brackts? with a hidden value of x, method that doesnt take any other parameters
    def x(self, value):
        self._x = value  # setter method

    @property
    def y(self):
        return self._y

    @property
    def colour(self):
        return self._colour

    @classmethod #a method that applies to the class as a whole, matter where it will apply as a whole
    def add_colour(cls, colour):
        """
        adds a new valid colour for our class
        :param colour:
        :return:
        """
        cls.COLOURS.append(colour)
    @staticmethod # functions that have nothing to do with the parameters of class, affects the class output not inputs,
    def from_tuple(coordinate, colour="red"):
        """
        creates a new point from a tuple rather than 2 individual values
        :param coordinate:
        :param colour:
        :return:
        """
        x, y = coordinate
        return AdvancedPoint(x, y, colour)
    @staticmethod
    def distance_2_points(p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) **2)**0.5

    def distance_to_other(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y)** 2) ** 0.5


AdvancedPoint.add_colour("rojo")
p = AdvancedPoint(1,2,"rojo")
print(p.x)
print(p)
print(p.distance_orig())
p2 = AdvancedPoint.from_tuple((3,2))
print(p2)
print(AdvancedPoint.distance_2_points(p,p2))
print(p.distance_to_other(p2))

