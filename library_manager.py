class Library:
    
    def __init__(self):
        self.books = {}  # Используем словарь для быстрого доступа
        self.borrowed_books = {}

    def add_book(self, title, author):

        if not isinstance(title, str) or not isinstance(author, str) or not title or not author:
            raise ValueError("Название и автор должны быть непустыми строками")
        if title in self.books:
            raise ValueError(f"Книга '{title}' уже существует")
        self.books[title] = {"author": author, "available": True}

    def borrow_book(self, title, user):

        if not isinstance(user, str) or not user:
            raise ValueError("Пользователь должен быть непустой строкой")
        if title in self.books and self.books[title]["available"]:
            self.books[title]["available"] = False
            self.borrowed_books[title] = user
            return True
        return False

    def return_book(self, title):
        if title in self.books and not self.books[title]["available"]:
            self.books[title]["available"] = True
            del self.borrowed_books[title]
            return True
        return False

    def get_available_books(self):
        return [title for title, info in self.books.items() if info["available"]]

    def get_borrowed_books(self):
        return list(self.borrowed_books.keys())

if __name__ == "__main__":
    lib = Library()
    lib.add_book("Python Basics", "John Doe")
    lib.add_book("AI Fundamentals", "Jane Smith")
    lib.borrow_book("Python Basics", "Alice")
    print("Доступные книги:", lib.get_available_books())
    print("Выданные книги:", lib.get_borrowed_books())
    lib.return_book("Python Basics")
    print("Доступные книги после возврата:", lib.get_available_books())