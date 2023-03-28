class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0


class Page(Book):
    def __init__(self, title, author, location, page):
        super().__init__(title, author, location)
        self.page = page

    def turn_page(self, page):
        self.page = page

