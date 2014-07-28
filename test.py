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
            self.assertFalse(func("function(){alert('foobar');}"))

    def test_guess(self):
        func = storysniffer.guess
        self.assertTrue(func(self.yes))
        self.assertFalse(func(self.no))
        self.assertFalse(func("http://www.facebook.com/foobar/"))
        self.assertFalse(func("http://careers.cnn.com/foobar/"))
        self.assertFalse(func("http://www.news.xxx/foobar/"))
        self.assertFalse(func("http://www.news.com/foobar.css"))
        self.assertFalse(func("http://www.news.com/foobar.jpg"))
        self.assertFalse(func("http://www.news.com/foobar.js"))


if __name__ == '__main__':
    if six.PY3:
        unittest.main(warnings='ignore')
    else:
        unittest.main()
