import pytest
from library_manager import Library

def test_add_book():
    lib = Library()
    lib.add_book("Test Book", "Test Author")
    assert "Test Book" in lib.books

def test_add_book_duplicate():
    lib = Library()
    lib.add_book("Test Book", "Test Author")
    with pytest.raises(ValueError):
        lib.add_book("Test Book", "Test Author")

def test_borrow_book_success():
    lib = Library()
    lib.add_book("Test Book", "Test Author")
    assert lib.borrow_book("Test Book", "User1") == True

def test_borrow_book_invalid_user():
    lib = Library()
    lib.add_book("Test Book", "Test Author")
    with pytest.raises(ValueError):
        lib.borrow_book("Test Book", "")

def test_return_book_success():
    lib = Library()
    lib.add_book("Test Book", "Test Author")
    lib.borrow_book("Test Book", "User1")
    assert lib.return_book("Test Book") == True

def test_get_available_books():
    lib = Library()
    lib.add_book("Book1", "Author1")
    lib.add_book("Book2", "Author2")
    lib.borrow_book("Book1", "User1")
    assert lib.get_available_books() == ["Book2"]