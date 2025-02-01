import pytest
from classifytriangle import classify_triangle

def test_equilateral():
    assert classify_triangle(2, 2, 2) == "Equilateral"

def test_isosceles():
    assert classify_triangle(5, 5, 8) == "Isosceles"
    assert classify_triangle(5, 8, 5) == "Isosceles"
    assert classify_triangle(8, 5, 5) == "Isosceles"
    

def test_scalene():
    assert classify_triangle(7, 5, 3) == "Scalene"
    assert classify_triangle(5, 6, 7) == "Scalene"

def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene and Right"
    assert classify_triangle(5, 12, 13) == "Scalene and Right"

def test_invalid_triangle():
    assert classify_triangle(1, 2, 3) == "Does not form a valid triangle"
    assert classify_triangle(-4, 4, 5) == "Does not form a valid triangle"
    assert classify_triangle(-3, -4, 2) == "Does not form a valid triangle"