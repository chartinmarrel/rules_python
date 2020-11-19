import unittest

from lib.main import hello


class TestHello(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "hello")
