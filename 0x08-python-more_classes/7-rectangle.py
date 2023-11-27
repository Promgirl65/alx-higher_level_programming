#!/usr/bin/python3
"""class which defines a Rectangle"""

class Rectangle:
    """Represents a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area Of Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter Of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """Represents a diagram of Rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """Returns a String representation of Rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a Message for every deleted object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

