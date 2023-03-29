class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_obj = dict_obj
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.dict_obj:
            raise StopIteration
        for key, value in self.dict_obj.items():
            del self.dict_obj[key]
            return (key, value)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

