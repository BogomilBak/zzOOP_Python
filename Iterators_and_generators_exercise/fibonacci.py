def fibonacci():
    first = 0
    yield first
    second = 1
    yield second
    while True:
        number = first + second
        yield number
        first, second = second, number

generator = fibonacci()
for i in range(20):
    print(next(generator))
