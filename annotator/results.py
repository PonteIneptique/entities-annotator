import re
from typing import List

__all__ = ["Match"]


class Match:
    """ Captures information about each match, keeping in memory the search word
    and the link"""

    words: List[str]
    match: str

    def __init__(self, words: List[str], match: str):
        self.words: List[str] = words
        self.match: str = match

        for word_index, word in enumerate(words):
            if word.startswith("#") and word.endswith("#"):
                self.match = word.replace("#", "")
                self.words[word_index] = self.match

    def __str__(self):
        return " ".join(self.words)

    def _format_match(self, w: str) -> str:
        """ Format the match """
        if w == self.match:
            return "<span class=\"kwic\">"+w+"</span>"
        return w

    def __repr__(self) -> str:
        return " ".join([
            self._format_match(w)
            for w in self.words
        ])
