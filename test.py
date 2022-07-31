"""Test the module."""
from storysniffer import StorySniffer


def test_guess():
    """Test guesses."""
    client = StorySniffer()
    func = client.guess

    yes = "http://www.washingtonpost.com/investigations/us-intelligence-mining-data-from-nine-us-internet-companies-in-broad-secret-program/2013/06/06/3a0c0da8-cebf-11e2-8845-d970ccb04497_story.html"
    absolute_yes = "/investigations/us-intelligence-mining-data-from-nine-us-internet-companies-in-broad-secret-program/2013/06/06/3a0c0da8-cebf-11e2-8845-d970ccb04497_story.html"
    no = "http://www.cnn.com/"
    absolute_no = "/"
    busted = "foobar"

    assert func(yes)
    assert func(no) is not True
    assert func(absolute_yes)
    assert func(absolute_no) is not True
    assert func(busted) is not True
    assert func("http://www.facebook.com/foobar/") is not True
    assert func("http://careers.cnn.com/foobar/") is not True
    assert func("http://www.news.xxx/foobar/") is not True
    assert func("http://www.news.com/foobar.css") is not True
    assert func("http://www.news.com/foobar.jpg") is not True
    assert func("http://www.news.com/foobar.js") is not True
    assert func(
        "http://www.latimes.com/local/westside/la-me-lightning-strikes-20140728-story.html"
    )
    assert func("http://www.latimes.com/local/la-me-water-use-war-20140727-story.html")
    assert func("http://www.latimes.com/opinion/") is not True
    assert func("http://www.latimes.com/opinion/editorials/") is not True
    assert func("http://www.news.com/story/story.html")
    assert func(
        "http://www.cnn.com/video/data/2.0/video/us/2014/07/23/hln-husband-emails-sex-spreadsheet.hln.html?hpt=hp_t4"
    )
