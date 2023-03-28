class vowels:
    def __init__(self, letter):
        self.letter = letter
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.letter):
            raise StopIteration
        result = self.letter[self.index]
        while not result.lower() in ['a', 'e', 'i', 'u', 'y', 'o']:
            result = self.letter[self.index]
            self.index += 1
        self.index += 1
        return result


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
