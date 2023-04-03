def even_parameters(func):
    def wrapper(*args):
        for element in args:
            if not isinstance(element, int) or not element % 2 == 0:
                return "Please use only even numbers!"
        result = func(*args)
        return result

    return wrapper


@even_parameters
def add(a, b):
    return a + b


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 9, 8))


