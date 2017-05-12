class Rectangle:
    """
    This is the rectangle class.  It accepts either a floating-point length and width as input or
    it will accept the top-left and bottom-right points as tuples.  Raises an exception if no floating
    point value is given.

    Use:
        shape = Rectangle((2.0, 3.5), (9.0, 9.5))
        shape = Rectangle(10.0, 20.0)

    Methods:
        void calclength(float, float)
        void calcwidth(float, float)
        void calcperimeter()
        void calcarea()
        bool is_circle()
    """
    def __init__(self, a, b):
        if (isinstance(a, tuple)):
            self.calclength(a, b)
        else:
            self.length = a
        if (isinstance(b, tuple)):
            self.calcwidth(a, b)
        else:
            self.width = b
        self.calcperimeter()
        self.calcarea()

    def __setattr__(self, key, value):
        if (isinstance(value, float) and value > 0):
            super(Rectangle, self).__setattr__(key, value)
        else:
            raise Exception

    def calclength(self, a, b):
        self.length = b[0] - a[0]

    def calcwidth(self, a, b):
            self.width = b[1] - a[1]

    def calcperimeter(self):
        self.perimeter = self.length * 2 + self.width * 2

    def calcarea(self):
        self.area = self.length * self.width

    def is_circle(self):
        return self.width == self.length


def main():
    "Main driver function"
    try:
        shape = Rectangle(10.00, 5.00)
        print("Rectangle 1:")
        print("Rectangle length is: {:.2f}".format(shape.length))
        print("Rectangle width is: {:.2f}".format(shape.width))
        print("Rectangle perimeter is: {:.2f}".format(shape.perimeter))
        print("Rectangle area is: {:.2f}".format(shape.area))
        print("Rectangle {} a circle".format((shape.is_circle()) and "is" or "is not"))
        print()
        print("Rectangle 2:")
        shape = Rectangle((2.0, 5.0), (10.0, 12.0))
        print("Rectangle length is: {:.2f}".format(shape.length))
        print("Rectangle width is: {:.2f}".format(shape.width))
        print("Rectangle perimeter is: {:.2f}".format(shape.perimeter))
        print("Rectangle area is: {:.2f}".format(shape.area))
        print("Rectangle {} a circle".format((shape.is_circle()) and "is" or "is not"))
        print()
        print("Rectangle 3:")
        shape = Rectangle(5.0, 5.0)
        print("Rectangle length is: {:.2f}".format(shape.length))
        print("Rectangle width is: {:.2f}".format(shape.width))
        print("Rectangle perimeter is: {:.2f}".format(shape.perimeter))
        print("Rectangle area is: {:.2f}".format(shape.area))
        print("Rectangle {} a circle".format((shape.is_circle()) and "is" or "is not"))
        print()
    except Exception:
        print("Error creating rectangle, bad input!")


if __name__ == "__main__":
    main()