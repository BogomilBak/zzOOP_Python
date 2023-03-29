class take_skip:
    def __init__(self, step, count):
        self.count = count
        self.step = step
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        result = self.value
        self.count -= 1
        self.value += self.step
        return result


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
