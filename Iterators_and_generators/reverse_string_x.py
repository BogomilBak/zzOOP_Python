def reverse_text(param):
    index = -1
    while abs(index) <= len(param):
        yield param[index]
        index -= 1


for char in reverse_text("step"):
    print(char, end='')
