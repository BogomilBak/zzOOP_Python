def genrange(start, end):
    n = start
    while n < end + 1:
        yield n
        n += 1


print(list(genrange(1, 10)))