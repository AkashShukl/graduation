import unittest

from main import Graduation

class GraduationTests(unittest.TestCase):
    def setUp(self):
        self.g = Graduation(5, 4)

    def test_number_of_ways_to_attend(self):
        self.assertEqual(self.g.number_of_ways_to_attend(), "14/29")

    def test_number_of_ways_to_attend_with_different_parameters(self):
        g = Graduation(10, 4)
        self.assertEqual(g.number_of_ways_to_attend(), "372/773")

if __name__ == '__main__':
    unittest.main() 