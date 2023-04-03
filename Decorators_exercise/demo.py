def recu(n):
    if n == 2:
        return n / 2
    return recu(n - 1) * n


a = 64
print(recu(a))
