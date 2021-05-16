import unittest
import color

class TestColor(unittest.TestCase):

    def test_color(self):
        self.assertEqual(color.color(), '{"color": "red"}', "Should be red")

if __name__ == '__main__':
    unittest.main()