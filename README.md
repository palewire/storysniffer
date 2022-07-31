storysniffer
============

Inspect a URL and estimate if it links to news story

Getting started
---------------

Install the package from the Python Package Index.

```bash
$ pip install storysniffer
```

The ``guess`` method offers a hard yes or no estimate. But keep in mind that this package is still embryonic and don't take its answer too seriously.

```python
import storysniffer

storysniffer.guess(
    "http://www.washingtonpost.com/investigations/us-intelligence-mining-data-from-nine-us-internet-companies-in-broad-secret-program/2013/06/06/3a0c0da8-cebf-11e2-8845-d970ccb04497_story.html"
)
True
storysniffer.guess("http://www.washingtonpost.com/")
False
storysniffer.guess("https://twitter.com/bartongellman")
False
```

Credits
-------

Past work on this project was sponosored by The Reynolds Journalism Institute and the University of Missouri.
