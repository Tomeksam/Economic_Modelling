import random

from point import Point

class ColourPoint(Point): #inheritence
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

    def __str__(self):
        return f"<{self.colour}: {self.x}, {self.y}>"

if __name__ == "__main__":
    p = ColourPoint(1,2,"red")
    print(p)
    colours = ["red", "green", "blue", "yellow", "black", "magenta", "cyan", "white", "burgundy", "periwinkle", "marsala"]
    colour_points = []
    for i in range(10):
        colour_points.append(
            ColourPoint(random.randint(-10,10),
                        random.randint(-10,10), #third parameter, colour
                        random.choice(colours)))

    print(colour_points)
    colour_points.sort()
    print(colour_points)
