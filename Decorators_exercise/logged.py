import functools


def logged(func):
    @functools.wraps(func)
    def wrapper(*args):
        result = f"you called {func.__name__}{args}\n" + f"it returned {func(*args)}"
        return result

    return wrapper


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))

