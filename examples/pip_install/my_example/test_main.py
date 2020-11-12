import sys
import unittest

from hello.main import hello


class TestHello(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "hello")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover(".")
    runner = unittest.TextTestRunner()
    sys.exit(not runner.run(suite).wasSuccessful())
