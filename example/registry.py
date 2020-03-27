from abc import ABCMeta
from importlib import import_module
from pathlib import Path
from typing import Dict, cast


registry: Dict[str, "RegisterMetaClass"] = {}


class Registry:
    @classmethod
    def supported_languages(cls):
        if not registry:
            cls.load_modules()
        languages = iter(registry.keys())
        return set(languages)

    @classmethod
    def get_language_class(cls, name: str):
        if not registry:
            cls.load_modules()
        return registry[name]

    @classmethod
    def get_language_instance(cls, name):
        return cls.get_language_class(name)()

    @staticmethod
    def load_modules():
        root = Path(__file__).resolve().parent

        modules = root.glob("languages/*/*.py")
        if not modules:
            raise ValueError("Found no language module.")

        for module in modules:
            module = str(module)
            if not module.lower().endswith("__init__.py"):
                module = module[
                    module.index("example/languages") : -len(".py")
                ].replace("/", ".")
                import_module(module)


class RegisterMetaClass(ABCMeta):
    def __new__(cls, class_name, bases, namespace, language):
        namespace["language"] = language
        namespace["lang_code"] = language.split("-")[0].lower() if language else None

        new = cast(
            "RegisterMetaClass", super().__new__(cls, class_name, bases, namespace)
        )
        if not language:
            return new

        registry[language] = new
        return new

    def __init__(cls, *args, language, **kwargs):
        super().__init__(*args, **kwargs)
