import time


def count_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        stop = time.time()
        print(f'Function time is {stop-start}')
        return f
    return wrapper
