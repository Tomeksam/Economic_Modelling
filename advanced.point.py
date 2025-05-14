from colour_point2 import ColourPoint, PointException
# this is demonstrating the factory method as we return a new instance of the class

class AdvancedPoint(ColourPoint): # lets define a lsit of acceptable colours
    COLOURS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"] # not a attribute per instance, its the same for each class

    def __init__(self, x, y, colour):
        """
        Constructor: Validates input colour and sets x, y, and colour as private attributes.
        """
        if colour not in self.COLOURS:
            raise PointException(f"Invalid colour bro must be one of the ones i{self.COLOURS}")
        self._x = x
        self._y = y
        self._colour = colour

    @property 
    def x(self):
        """
        Getter: Returns x-coordinate.
        """
        return self._x # getter method

    @property  
    def x(self, value):
        """
        Setter: Updates x-coordinate to new value.
        """
        self._x = value  # setter method

    @property
    def y(self):
        """
        Getter: Returns y-coordinate.
        """
        return self._y

    @property
    def colour(self):
        """
        Getter: Returns colour attribute.
        """
        return self._colour

    @classmethod 
    def add_colour(cls, colour):
        """
        Class method: Adds a new allowed colour to COLOURS list.
        """
        cls.COLOURS.append(colour)

    @staticmethod 
    def from_tuple(coordinate, colour="red"):
        """
        Static method (factory): Creates instance from coordinate tuple and optional colour.
        """
        x, y = coordinate
        return AdvancedPoint(x, y, colour)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Static method: Returns Euclidean distance between two point instances.
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y)**2)**0.5

    def distance_to_other(self, p):
        """
        Instance method: Returns distance from current object to another point.
        """
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
