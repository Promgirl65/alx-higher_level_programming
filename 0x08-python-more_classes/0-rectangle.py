#!/usr/bin/python3
"""class that defines a Rectangle."""

class Rectangle:
    """An empty Rectangle class"""
    Pass

1-rectangle.py
#!/usr/bin/python3
"""A class which defines a rectangle"""

class Rectangle:
    """this class represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width"""
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

