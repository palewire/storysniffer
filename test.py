import six
import unittest


class SniffTest(unittest.TestCase):

    def test_pass(self):
        pass


if __name__ == '__main__':
    if six.PY3:
        unittest.main(warnings='ignore')
    else:
        unittest.main()
