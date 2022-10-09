import unittest
import return_addtion
import triangle_area

class MyTestCase(unittest.TestCase):

    def test_return_addtion(self):

        self.assertEqual(15, return_addtion.addTwo(7, 8))
        self.assertEqual(45, return_addtion.addTwo(40, 5))
        # Add two more tests of your own below here
        self.assertEqual(-1, return_addtion.addTwo(2, -3))
        self.assertEqual(-20, return_addtion.addTwo(-12, -8))

'''
    def test_triangle_area(self):
        self.assertEqual(6.0, triangle_area.area(3, 4, 5))


if __name__ == '__main__':
    unittest.main()
'''
