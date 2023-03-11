from .user import User
class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {} # {Author: [str, str]}
        self.rented_books = {} # {Username: {book name: days to return}}

    def get_book(self, author, book_name, days_to_return, user: User):
        if author in self.books_available.keys():
            if book_name in self.books_available[author]:
                user.books.append(book_name)
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}
                self.rented_books[user.username][book_name] = days_to_return
                self.books_available[author].remove(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        for key in self.rented_books.values():
            if book_name in key:
                return f'The book "{book_name}" is already rented and will be available in {key[book_name]} days!'

    def return_book(self, author, book_name, user):
        if book_name in user.books:
            user.books.remove(book_name)
            self.rented_books[user.username].pop(book_name)
            self.books_available[author].append(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"

