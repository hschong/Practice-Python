import time


# not using decorator
def timestamps(func):
    def wrapper():
        start = time.perf_counter()
        print(f"start: {start}, {func.__name__}")
        func()
        end = time.perf_counter()
        print(f"end: {end}, {func.__name__}")

    return wrapper


def hello():
    print('hello')


def world():
    print('world')


hello_timestamps = timestamps(hello)
world_timestamps = timestamps(world)
hello_timestamps()
world_timestamps()


# using decorator
def deco_timestamps(func):
    def wrapper():
        start = time.perf_counter()
        print(f"start: {start}, {func.__name__}")
        func()
        end = time.perf_counter()
        print(f"end: {end}, {func.__name__}")

    return wrapper


@deco_timestamps
def deco_hello():
    print('hello')


@deco_timestamps
def deco_world():
    print('world')


deco_hello()
deco_world()
