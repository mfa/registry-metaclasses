import pytest
from example.registry import Registry


def test_registry_collected():
    assert Registry.supported_languages() == {"de-DE", "en-US"}


@pytest.mark.parametrize("language_code,string,result", (
    ("de-DE", "a", "rendered (DE): a"),
    ("en-US", "a", "rendered: a"),
))
def test_registry_example_results(language_code, string, result):
    assert Registry.get_language_instance(language_code).render(string) == result
