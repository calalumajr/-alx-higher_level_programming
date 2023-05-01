#!/usr/bin/python3
class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

