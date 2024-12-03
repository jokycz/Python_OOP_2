from functools import wraps
from typing import Callable, Dict

def format_as_plain_text(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        text_output = []
        for key, value in data.items():
            text_output.append(f"{key}: {value}")
        return "\n".join(text_output)
    return wrapper