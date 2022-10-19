import unittest
import assignment_three


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)





'''
def test_input(self):
     with mock.patch('builtins.input', return_value="3"):
        assert type(assignment_three.get_side_length()) == int

'''
if __name__ == '__main__':
    unittest.main()
