import unittest
from triangle import Triangle


class TestTriangleUnit(unittest.TestCase):

    def setUp(self):
        self.first = Triangle(9, 8, 7)
        print("Triangle 7,8,9 created as 'first")

    def tearDown(self):
        del self.first
        print("Triangle 7,8,9  'first deleted")


    def test_triangle_eq(self):
        second = Triangle(7, 9, 8)
        self.assertEqual(self.first, second)

    def test_triangle_perimetr(self):
        self.assertEqual(self.first.perimetr(), 24)

    def test_triangle_square(self):
        second = Triangle(7, 9, 8)
        self.assertEqual(self.first.square(), second.square())
    def test_triangle_equal_to_other(self):
        second = Triangle(7, 9, 8)
        assert self.first.with_same_corners(second)
        self.assertTrue(self.first.with_same_corners(second))
    def test_triangle_is_right_angled(self):
        second = Triangle(7, 8, 9)
        self.assertFalse(self.first.is_right_angled(), second.is_right_angled())
    def test_is_right_triangle(self):
        second = Triangle(7, 9, 8)
        self.assertFalse(self.first.is_right_triangle(), second.is_right_triangle())
    def test_two_sides_eq(self):
        second = Triangle(7, 9, 8)
        self.assertFalse(self.first.two_sides_eq(), second.two_sides_eq)


if __name__ == '__main__':
    unittest.main()