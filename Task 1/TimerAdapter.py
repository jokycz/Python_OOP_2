import time
import functools

def timer_adapter(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        # Správné chování pro dekoraci metod
        start_time = time.time()
        result = func(self, *args, **kwargs)  # Voláme původní metodu správně
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Doba provádění: {elapsed_time:.4f} sekund")
        return result
    return wrapper