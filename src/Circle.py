import math
from abc import ABC

from src.Rectangle import Figure


class Circle(Figure, ABC):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Can't create Circle")
        super().__init__()
        self.radius = radius
        self.name = f"Circle {radius}"

    def get_area(self):
        return round(math.pi * (self.radius**2))

    def get_perimeter(self):
        return round(2 * self.radius * math.pi)

