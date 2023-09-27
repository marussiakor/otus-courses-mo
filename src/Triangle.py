import math
from abc import ABC

from src.Figure import Figure


class Triangle(Figure, ABC):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Can't create Triangle")
        super().__init__()
        self.side_a = float(side_a)
        self.side_b = float(side_b)
        self.side_c = float(side_c)
        self.name = f"Triangle {side_a} and {side_b} and {side_c}"

    def get_area(self):
        hp = round((self.side_a + self.side_b + self.side_c) / 2)
        return round(math.sqrt(hp - self.side_a)*(hp - self.side_b)*(hp - self.side_c))

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

