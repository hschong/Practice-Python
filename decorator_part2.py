# passing func's arguments into wrapper
def print_add(func):
    def wrapper(a, b):
        result = func(a, b)
        print(f'func = {func.__name__}, a = {a}, b = {b}, result = {result}')
        return result
    return wrapper


@print_add
def add(a, b):
    return a+b


print(add(3, 4))


# passing decorator's argument into wrapper
def is_multiple(x):
    def deco(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f'func = {func.__name__}, *args: {args}, **kwargs: {kwargs}')

            if (result % x) == 0:
                print(f'{result} is a mupltiplication of {x}')
            else:
                print(f'{result} is not a mupltiplication of {x}')

            return result
        return wrapper
    return deco


@is_multiple(3)
def get_min1(*args):
    return min(args)


@is_multiple(3)
def get_max1(**kwargs):
    return max(kwargs.values())


print(get_max1(x=10, y=20, z=5))
print(get_min1(10, 20))


# variadic arguments
def print_arguments(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'func = {func.__name__}, *args: {args}, **kwargs: {kwargs}')
        return result
    return wrapper


@print_arguments
def get_max(*args):
    return max(args)


@print_arguments
def get_min(**kwargs):
    return min(kwargs.values())


print(get_max(10, 20))
print(get_min(x=10, y=20, z=5))
