from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
import pytest

from src.Triangle import Triangle


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(4, 6, 24, 20)])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(-4, -6, -24, -20),
                          (0, 0, 0, 0)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.name == f"Rectangle {side_a} and {side_b}"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(4, 16, 16),
                          (5, 25, 20)])
def test_sq(side_a, area, perimeter):
    s = Square(side_a)
    assert s.name == f"Square {side_a}"
    assert s.get_area() == area
    assert s.get_perimeter() == perimeter


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(2, 13, 13),
                          (-5, 25, 20)])
def test_circle(radius, area, perimeter):
    c = Circle(radius)
    assert c.name == f"Circle {radius}"
    assert c.get_area() == area
    assert c.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(2, 4, 4, 2, 10),
                          (-5, 0, 4, 7, 9)])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.name == f"Triangle {side_a} and {side_b} and {side_c}"
    assert t.get_area() == area
    assert t.get_perimeter() == perimeter


def test_add_area():
    r = Rectangle(2, 5)
    s = Square(5)
    c = Circle(3)
    t = Triangle(2, 5, 8)
    assert r.add_area(s) == 34
    assert c.add_area(r) == 42
    assert t.add_area(s) == 20


def test_add_area_negative():
    r = Rectangle(2, 5)
    c = Circle(10)
    assert r.add_area(c) == 44



