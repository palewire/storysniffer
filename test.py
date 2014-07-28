import six
import unittest
import storysniffer


class SniffTest(unittest.TestCase):

    def setUp(self):
        self.yes = "http://www.washingtonpost.com/investigations/us-\
intelligence-mining-data-from-nine-us-internet-companies-in-broad-secret-\
program/2013/06/06/3a0c0da8-cebf-11e2-8845-d970ccb04497_story.html"
        self.no = "http://www.cnn.com"
        self.busted = "foobar"

    def test_busted(self):
        with self.assertRaises(ValueError):
            storysniffer.guess(self.busted)

    def test_guess(self):
        self.assertTrue(storysniffer.guess(self.yes))
        self.assertFalse(storysniffer.guess(self.no))


if __name__ == '__main__':
    if six.PY3:
        unittest.main(warnings='ignore')
    else:
        unittest.main()
