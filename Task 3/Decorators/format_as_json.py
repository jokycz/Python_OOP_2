from functools import wraps
from typing import Callable, Dict
import json

def format_as_json(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return json.dumps(data, indent=4)
    return wrapper