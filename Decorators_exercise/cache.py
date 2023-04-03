def cache(func):
    log = {}

    def wrapper(args):
        if args in log:
            return log[args]
        result = func(args)
        log[args] = result
        return result
    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(3))
print(fibonacci.log)


