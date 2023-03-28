class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, content):
        return Book(content)


class Printer:
    def get_book(self, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book