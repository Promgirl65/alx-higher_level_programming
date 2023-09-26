#!/usr/bin/python3
"""To Define A Square Module."""


class Square:
    """Represents the Square Class."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing the Square size and Position.
        Args:
            size: size of Square (int)
            position: Coordinates of Square
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """"Property of Square Size
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Property of Square coordinates
        Raises:
            TypeError: if value is not a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of Square
        Args: value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """To get the Area of Square
        Returns: The new Square Area.
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end='')
