import unittest
from models.models import Book
from src.storage import JSONPersistence
from src.library import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Подготовка библиотеки для тестов."""
        self.persistence = JSONPersistence("tests/test_library.json")
        self.library = Library(self.persistence)
        self.library.books = [
            Book(1, "Book One", "Author One", 2021),
            Book(2, "Book Two", "Author Two", 2022),
        ]

    def tearDown(self):
        """Очистка временных данных."""
        self.persistence.save([])

    def test_add_book(self):
        """Тест добавления книги."""
        self.library.add_book("Book Three", "Author Three", 2023)
        self.assertEqual(len(self.library.books), 3)
        added_book = self.library.books[-1]
        self.assertEqual(added_book.title, "Book Three")
        self.assertEqual(added_book.author, "Author Three")
        self.assertEqual(added_book.year, 2023)
        self.assertEqual(added_book.status, "в наличии")

    def test_add_book_with_default_values(self):
        """Тест добавления книги с дефолтными значениями."""
        self.library.add_book(title='', author='', year='')
        added_book = self.library.books[-1]
        self.assertEqual(added_book.title, "У книги нет названия")
        self.assertEqual(added_book.author, "У книги нет автора")
        self.assertEqual(added_book.year, "У книги неизвестен год выпуска")

    def test_delete_book(self):
        """Тест удаления книги."""
        result = self.library.delete_book(1)
        self.assertTrue(result)
        self.assertEqual(len(self.library.books), 1)
        self.assertIsNone(self.library.find_book_by_id(1))

    def test_delete_book_not_found(self):
        """Тест удаления несуществующей книги."""
        result = self.library.delete_book(999)
        self.assertFalse(result)

    def test_find_book_by_id(self):
        """Тест поиска книги по ID."""
        book = self.library.find_book_by_id(1)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Book One")

    def test_find_book_by_id_not_found(self):
        """Тест поиска книги по ID, которая не существует."""
        book = self.library.find_book_by_id(999)
        self.assertIsNone(book)

    def test_search_books(self):
        """Тест поиска книг по полю."""
        results = self.library.search_books("One", "title")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Book One")

    def test_search_books_not_found(self):
        """Тест поиска книг, которые не существуют."""
        results = self.library.search_books("Nonexistent", "title")
        self.assertEqual(len(results), 0)

    def test_update_status(self):
        """Тест изменения статуса книги."""
        result = self.library.update_status(1, "выдана")
        self.assertTrue(result)
        self.assertEqual(self.library.find_book_by_id(1).status, "выдана")

    def test_update_status_book_not_found(self):
        """Тест изменения статуса несуществующей книги."""
        result = self.library.update_status(999, "выдана")
        self.assertFalse(result)
