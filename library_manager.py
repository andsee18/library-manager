# Система управления библиотекой
class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author, "available": True})

    def borrow_book(self, title, user):
        for book in self.books:
            if book["title"] == title and book["available"]:
                book["available"] = False
                self.borrowed_books[title] = user
                return True
        return False

    def return_book(self, title):
        for book in self.books:
            if book["title"] == title and not book["available"]:
                book["available"] = True
                del self.borrowed_books[title]
                return True
        return False

    def get_available_books(self):
        available = []
        for book in self.books:
            if book["available"]:
                available.append(book["title"])
        return available

    def get_borrowed_books(self):
        return list(self.borrowed_books.keys())

# Пример использования
if __name__ == "__main__":
    lib = Library()
    lib.add_book("Python Basics", "John Doe")
    lib.add_book("AI Fundamentals", "Jane Smith")
    lib.borrow_book("Python Basics", "Alice")
    print("Доступные книги:", lib.get_available_books())
    print("Выданные книги:", lib.get_borrowed_books())
    lib.return_book("Python Basics")
    print("Доступные книги после возврата:", lib.get_available_books())