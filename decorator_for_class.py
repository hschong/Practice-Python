import time


class TimeStamps():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        start = time.perf_counter()
        result = self.func(*args)
        end = time.perf_counter()
        print(f'func = {self.func.__name__}, start = {start}')
        print(f'func = {self.func.__name__}, end = {end}')
        return result


@TimeStamps
def get_max(*args):
    return max(args)


print(f'get_max(20, 50, 60, 7) = {get_max(20, 50, 60, 7)}')
