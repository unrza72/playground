import unittest

from playground.some_module import add


class Example(unittest.TestCase):

    def test_add(self):

        a = 2
        b = 4

        c = add(a, b)

        self.assertEqual(c, a+b)