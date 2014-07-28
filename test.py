import six
import unittest
import storysniffer


class SniffTest(unittest.TestCase):

    def setUp(self):
        self.yes = "http://www.washingtonpost.com/investigations/us-\
intelligence-mining-data-from-nine-us-internet-companies-in-broad-secret-\
program/2013/06/06/3a0c0da8-cebf-11e2-8845-d970ccb04497_story.html"
        self.absolute_yes = "/investigations/us-\
intelligence-mining-data-from-nine-us-internet-companies-in-broad-secret-\
program/2013/06/06/3a0c0da8-cebf-11e2-8845-d970ccb04497_story.html"
        self.no = "http://www.cnn.com/"
        self.absolute_no = "/"
        self.busted = "foobar"

    def test_busted(self):
        with self.assertRaises(ValueError):
            storysniffer.guess(self.busted)
            self.assertFalse(func("function(){alert('foobar');}"))
            self.assertFalse(func(self.absolute_yes))
            self.assertFalse(func(self.absolute_no))

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
        self.assertTrue(func("http://www.latimes.com/local/westside/\
la-me-lightning-strikes-20140728-story.html"))
        self.assertTrue(func("http://www.latimes.com/local/\
la-me-water-use-war-20140727-story.html"))
        self.assertFalse(func("http://www.latimes.com/opinion/"))


if __name__ == '__main__':
    if six.PY3:
        unittest.main(warnings='ignore')
    else:
        unittest.main()
