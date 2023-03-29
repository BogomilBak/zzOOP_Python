def get_primes(ll):
    for element in ll:
        count = 0
        for el in range(1, element + 1):
            if element % el == 0:
                count += 1
        if count == 2:
            yield element


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
