from ..base import ExampleBase


class Example_DE_DE(ExampleBase, language="de-DE"):
    def __init__(self):
        # i.e.
        # assert spacy.__version__[0:3] == "2.2"
        # self.nlp = spacy.load("de_core_news_sm")
        pass

    def render(self, lemma):
        return f"rendered (DE): {lemma}"
