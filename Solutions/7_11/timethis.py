# timethis.py

import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args,**kwargs)
        finally:
            end = time.time()
            print("%s.%s : %f" % (func.__module__,func.__name__,end-start))
    return wrapper

if __name__ == '__main__':
    @timethis
    def countdown(n):
        while n > 0:
            n-= 1

    countdown(1000000)
