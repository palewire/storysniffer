storysniffer
============

Inspect a URL and estimate if it links to news story

[![Build Status](https://travis-ci.org/pastpages/storysniffer.svg?branch=master)](https://travis-ci.org/pastpages/storysniffer)
[![PyPI version](https://badge.fury.io/py/storysniffer.png)](http://badge.fury.io/py/storysniffer)
[![Coverage Status](https://coveralls.io/repos/pastpages/storysniffer/badge.png?branch=master)](https://coveralls.io/r/pastpages/storysniffer?branch=master)

* Issues: [https://github.com/pastpages/storysniffer/issues](<https://github.com/pastpages/storysniffer/issues)
* Packaging: [https://pypi.python.org/pypi/storysniffer](https://pypi.python.org/pypi/storysniffer)
* Testing: [https://travis-ci.org/pastpages/storysniffer](https://travis-ci.org/pastpages/storysniffer)

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

This is a joint project of [PastPages.org](http://pastpages.org), The Reynolds Journalism Institute and the University of Missouri.
