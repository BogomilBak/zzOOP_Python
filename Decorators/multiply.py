from functools import wraps


def multiply(times):
    def decorator(func):
        def wrapper(args):
            return times * func(args)

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
