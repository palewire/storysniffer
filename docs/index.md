```{include} _templates/nav.html
```

# storysniffer

Inspect a URL and estimate if it links to news story.

## Getting started

Install this module

```bash
pipenv install storysniffer
```

Import the sniffer and load its machine-learning models.

```python
from storysniffer import StorySniffer

sniffer = StorySniffer()
```

Pass in a URL to get our estimate. `True` or `False` is returned.

```python
sniffer.guess(
    "https://www.latimes.com/la-me-michael-jackson-dead26-2009jun26-story.html"
)
```

If you have a text string, like the page's `<title>` tag or the contents of an `<a>` tag, you can pass that in as an additional clue.

```python
sniffer.guess(
    "https://www.latimes.com/la-me-michael-jackson-dead26-2009jun26-story.html",
    text="King of Pop is dead at 50",
)
```

That's it!

## About the model

Storysniffer makes it guess based on a machine-learning model. It is drawn from a supervised sample of links collected by the News Homepages project at [homepages.news](https://homepages.news). [Testing](https://github.com/palewire/storysniffer/blob/main/_notebooks/train.ipynb) has shown it is accurate in 96% of cases.

However, because its training sample is limited to news homepages, most of which are in English, it likely contains some bias. Accuracy may vary for links gathered from other sources and languages. Those interested in improving the model should join our [open-source effort](https://github.com/palewire/storysniffer).

## Credits

Past work on this project was sponosored by The Reynolds Journalism Institute and the University of Missouri.

## Links

* Docs: [palewi.re/docs/storysniffer/](https://palewi.re/docs/storysniffer/)
* Issues: [github.com/palewire/storysniffer/issues](https://github.com/palewire/storysniffer/issues)
* Packaging: [pypi.python.org/pypi/storysniffer](https://pypi.python.org/pypi/storysniffer)
* Testing: [github.com/palewire/storysniffer/actions](https://github.com/palewire/storysniffer/actions)
