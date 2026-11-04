# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")
        if not isinstance(height, int):
            raise TypeError("Height must be an integer")
        if width <= 0:
            raise ValueError("Width must be a positive integer")
        if height <= 0:
            raise ValueError("Height must be a positive integer")        
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    @staticmethod

    def is_square(width, height):
        """
        Checks if width and height have equal length.
        If they are equal, returns that the rectangle is a square.
        """
        if width == height:
            return True
        else:
            return False

    def area(width, height):
        """
        Calculates and returns the area of the rectangle.
        """
        area = width * height
        return area

    def perimeter(width, height):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        perimeter = 2 * width + 2 * height
        return perimeter