import re
from collections import defaultdict

from ..registry import RegisterMetaClass


class ExampleBase(metaclass=RegisterMetaClass, language=None):

    language: str

    def render(self, lemma):
        return f"rendered: {lemma}"
