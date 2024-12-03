from functools import wraps
from typing import Callable, Dict
import csv

def format_as_csv(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)

        # Pokud je data slovník, zabalíme ho do seznamu
        if isinstance(data, dict):
            data = [data]

        # Ověření, že data jsou seznam slovníků
        if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
            raise ValueError("Data pro CSV musí být seznam slovníků nebo slovník.")

        csv_output = []
        headers = data[0].keys()  # Klíče použijeme jako hlavičky
        csv_output.append(",".join(headers))  # Přidání hlavičky
        for row in data:
            csv_output.append(",".join(str(row[h]) for h in headers))  # Přidání hodnot
        return "\n".join(csv_output)

    return wrapper