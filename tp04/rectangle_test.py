import unittest
from Rectangle import Rectangle



class TestRectangle(unittest.TestCase):

    def test_rectangle_is_created(self):
        r = Rectangle(2,3)
        self.assertIsInstance(r,Rectangle)

    def test_rectangle_is_failed_with_negative_values(self):
        # r = Rectangle(-2,-3)
        # self.assertRaises(AssertionError,Rectangle,-2,-3)
        with self.assertRaises(AssertionError):
            r = Rectangle(-2,-3)
