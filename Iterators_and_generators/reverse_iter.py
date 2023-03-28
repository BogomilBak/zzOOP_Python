class reverse_iter:
    def __init__(self, my_list):
        self.my_list = my_list
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.index) > len(self.my_list):
            raise StopIteration
        value_to_return = self.my_list[self.index]
        self.index -= 1
        return value_to_return


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
