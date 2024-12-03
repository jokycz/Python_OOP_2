import os
import importlib
from typing import Callable, Dict

def load_decorators_from_directory(directory: str, base_module: str) -> Dict[str, Callable]:
    """
    Dynamicky načte všechny dekorátory ze složky a vrátí je jako slovník.
    :param directory: Cesta ke složce s dekorátory.
    :param base_module: Základní modul, pod kterým jsou dekorátory.
    :return: Slovník {název_dekorátoru: dekorátor_funkce}.
    """
    decorators = {}
    for file_name in os.listdir(directory):
        if file_name.endswith(".py") and file_name != "__init__.py":
            module_name = file_name[:-3]  # Odebrání ".py"
            module_path = f"{base_module}.{module_name}"
            module = importlib.import_module(module_path)
            # Načítáme všechny objekty v modulu
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if callable(attr) and attr_name.startswith("format_as_"):
                    decorators[attr_name] = attr
    return decorators
