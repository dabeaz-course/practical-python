import time
from typing import Callable


def timethis(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__module__}.{func.__name__}: {end - start}')
        return result

    return wrapper
