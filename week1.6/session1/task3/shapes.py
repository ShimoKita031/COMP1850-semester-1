# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
# Make sure that it inherits properly from Shape!
class Circle:
    def __init__(self, position, radius):
        colour = "red"
        super().__init__(position, colour)
        self.radius = radius

    def set_radius(self, radius):
        if not isinstance(radius, int) or not isinstance(radius, float):
            raise TypeError("Radius must be an integer or float")
        if radius <= 0:
            raise ValueError("Radius must be a positive value")

    def __str__(self, radius, position):
        return f"red circle, radius {radius}, at {position}"

    def area(self, radius):
        area = radius * radius * math.pi()
        return area

    def perimeter(self, radius):
        perimeter = radius * 2 * math.pi()
        return perimeter