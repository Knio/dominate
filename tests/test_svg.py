
from dominate.tags import svg, circle, rectangle
import unittest


class TestSVG(unittest.TestCase):

    def test_circle(self):
        c = circle(cx="50", cy="50", r="40", stroke="black", stroke_width="3")
        self.assertEqual(c.render(),
                         '<circle cx="50" cy="50" r="40" stroke="black" stroke_width="3"></circle>')

    def test_rectangle(self):
        r = rectangle(width="250", height="300")
        self.assertEqual(r.render(),
                         '<rectangle height="300" width="250"></rectangle>')



if __name__ == '__main__':
    unittest.main()