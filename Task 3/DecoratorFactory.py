import os
import importlib
from typing import Callable, Dict


class DecoratorFactory:
    def __init__(self, directory: str, base_module: str):
        """
        Inicializuje factory a načte všechny dekorátory ze složky.
        :param directory: Cesta ke složce s dekorátory.
        :param base_module: Název modulu dekorátorů.
        """
        self.decorators = self._load_decorators(directory, base_module)

    def _load_decorators(self, directory: str, base_module: str) -> Dict[str, Callable]:
        """
        Načte všechny dekorátory ze složky a vrátí je jako slovník {název: dekorátor}.
        """
        decorators = {}
        for file_name in os.listdir(directory):
            if file_name.endswith(".py") and file_name != "__init__.py":
                module_name = file_name[:-3]
                module_path = f"{base_module}.{module_name}"
                module = importlib.import_module(module_path)
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if callable(attr) and attr_name.startswith("format_as_"):
                        decorators[attr_name] = attr
        return decorators

    def call_decorator(self, decorator_name: str, data: Callable[[], dict]) -> str:
        """
        Zavolá konkrétní dekorátor na vstupní data.
        :param decorator_name: Název dekorátoru.
        :param data: Funkce vracející vstupní data.
        :return: Výstup dekorátoru.
        """
        decorator = self.decorators.get(decorator_name)
        if not decorator:
            raise ValueError(f"Dekorátor '{decorator_name}' není registrován.")
        return decorator(data)()
