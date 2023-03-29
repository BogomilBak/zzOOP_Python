from itertools import permutations


def possible_permutations(ll):
    for element in permutations(ll):
        yield list(element)


[print(n) for n in possible_permutations([1, 2, 3])]
