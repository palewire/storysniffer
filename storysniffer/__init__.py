"""Inspect a URL and estimate if it links to news story."""
import os
import re
import typing
from pathlib import Path
from urllib.parse import urlparse

import dill
import pandas as pd
import tldextract


class StorySniffer:
    """Inspect a URL and estimate if it links to news story."""

    THIS_DIR = Path(__file__).parent.absolute()

    # A list of URL parts that probably won't link to new stories
    DOMAIN_BLACKLIST = (
        "google",
        "twitter",
        "facebook",
        "doubleclick",
        "eventbrite",
        "youtube",
        "vimeo",
        "instagram",
        "ceros",
        "legacy",
        "pinterest",
    )

    SUBDOMAIN_BLACKLIST = (
        "careers",
        "mail",
        "account",
        "events",
        "help",
    )

    PATH_BLACKLIST = (
        "",
        "/",
        "/privacy/",
        "/about/",
    )

    EXT_BLACKLIST = (
        ".js",
        ".css",
        ".jpg",
        ".gif",
        ".png",
    )

    # A list of URL parts we think will link to stories
    PATHPART_WHITELIST = (
        "/story",
        "/stories",
        "/article",
        "/feature",
        "/featured",
        "/blog",
        "/interactive",
        "/graphic",
        "/video",
        "/post",
        "/projects",
    )

    # A list of url parts that we are sure don't link to stories
    PATHPART_BLACKLIST = (
        "/sponsored/",
        "/sponsored-content/",
        "/tag/",
        "/category/",
    )

    def __init__(self):
        """Initialize a new sniffer."""
        self.path_and_text_model = self.open_pickle("path-and-text-model.pickle")
        self.path_only_model = self.open_pickle("path-only-model.pickle")

    def open_pickle(self, path: str):
        """Open the provided pickle."""
        with open(self.THIS_DIR / path, "rb") as fh:
            return dill.load(fh)

    def tidy_text(self, t: str) -> str:
        """Clean up the provided text string."""
        t = t.strip()
        t = t.replace("\n", "")
        t = t.replace("\t", "")
        t = t.lower()
        t = re.sub("<[^<]+?>", "", t)
        t = " ".join(t.split())
        return t

    def guess(self, url: str, text: typing.Optional[str] = None) -> bool:
        """Estimate if the provided URL links to a news story."""
        # Drop any nulls
        if not url or pd.isnull(url) or not url.strip():
            return False

        # Pull out the data we need
        urlparts = urlparse(url)
        path = urlparts.path
        tld = tldextract.extract(url)

        # Drop anything we're certain isn't a story
        if tld.domain in self.DOMAIN_BLACKLIST:
            return False
        elif tld.subdomain in self.SUBDOMAIN_BLACKLIST:
            return False
        elif path in self.PATH_BLACKLIST:
            return False
        elif os.path.splitext(path)[1] in self.EXT_BLACKLIST:
            return False

        # Pick which model we're using, based on the input
        if text:
            text = self.tidy_text(text)
            model = self.path_and_text_model
        else:
            model = self.path_only_model

        # Run a prediction
        data = [dict(path=path, text=text)]
        prediction = model.predict(data)[0] == 1

        # If it's False but it has one of our whitelisted slugs, overturn the decision
        if not prediction:
            if path.startswith(self.PATHPART_WHITELIST) and len(path) > 10:
                if "-" in path or path.endswith(".html"):
                    return True

        # If it's True but it starts with a bad prefix knock it out
        if prediction and path.startswith(self.PATHPART_BLACKLIST):
            return False

        # Return the result
        return prediction
