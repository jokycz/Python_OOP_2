import json
from typing import Dict
from DecoratorFactory import DecoratorFactory


class FinancialReport:
    def __init__(self, report_data: Dict[str, int], factory: DecoratorFactory, mapping_file: str):
        """
        Inicializuje finanční zprávu.
        :param report_data: Data zprávy {název: hodnota}.
        :param factory: Instance DecoratorFactory.
        :param mapping_file: Cesta k JSON souboru s mapováním IČO -> dekorátor.
        """
        self.report_data = report_data
        self.factory = factory
        self.mapping = self._load_mapping(mapping_file)

    def _load_mapping(self, mapping_file: str) -> Dict[str, str]:
        """Načte mapování IČO -> dekorátor z JSON souboru."""
        try:
            with open(mapping_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise ValueError(f"Chyba při načítání mapping souboru: {e}")

    def generate(self, ico: str) -> str:
        """
        Generuje zprávu pro zadané IČO.
        :param ico: IČO pro koho se zpráva generuje.
        :return: Zpráva jako formátovaný řetězec.
        """
        decorator_name = self.mapping.get(ico)
        if not decorator_name:
            raise ValueError(f"IČO {ico} nemá přiřazený dekorátor.")
        return self.factory.call_decorator(decorator_name, lambda: self.report_data)
