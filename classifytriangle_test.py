import unittest
from classifytriangle import classify_triangle

class TestTriangleClassification(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles")
        self.assertEqual(classify_triangle(4, 3, 3), "Isosceles")
        self.assertEqual(classify_triangle(3, 4, 3), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right")
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene and Right")
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Does not form a valid triangle")
        self.assertEqual(classify_triangle(0, 0, 0), "Does not form a valid triangle")
        self.assertEqual(classify_triangle(-1, 2, 3), "Does not form a valid triangle")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right")
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene and Right")
        self.assertEqual(classify_triangle(8, 15, 17), "Scalene and Right")

    def test_non_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 6), "Scalene")
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

if __name__ == "__main__":
    unittest.main()
