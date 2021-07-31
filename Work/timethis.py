import time
from typing import Callable


def timethis(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.time()
            print(f'{func.__module__}.{func.__name__}: {end - start}')

    return wrapper


if __name__ == '__main__':
    @timethis
    def countdown(n: int):
        while n > 0:
            n -= 1


    countdown(10000000)
