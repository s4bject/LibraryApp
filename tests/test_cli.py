import unittest
from unittest.mock import patch, MagicMock
from src.library import Library
from src.cli import LibraryCLI
from models.models import Book

class TestLibraryCLI(unittest.TestCase):

    def setUp(self):
        """Подготовка CLI для тестов."""
        self.library = MagicMock(spec=Library)
        self.cli = LibraryCLI(self.library)

    @patch("builtins.input", side_effect=["1", "", "", "", "6"])
    @patch("builtins.print")
    def test_add_book_with_defaults(self, mock_print, mock_input):
        """Тест команды добавления книги с дефолтными значениями."""
        self.cli.run()
        self.library.add_book.assert_called_once_with('', '', '')

    @patch("builtins.input", side_effect=["2", "1", "6"])
    @patch("builtins.print")
    def test_delete_book_command(self, mock_print, mock_input):
        """Тест команды удаления книги."""
        self.library.delete_book.return_value = True
        self.cli.run()
        self.library.delete_book.assert_called_once_with(1)

    @patch("builtins.input", side_effect=["4", "6"])
    @patch("builtins.print")
    def test_display_books_command(self, mock_print, mock_input):
        """Тест команды отображения всех книг."""
        self.library.display_books.return_value = [
            Book(1, "Test Title", "Test Author", 2024)
        ]
        self.cli.run()
        self.library.display_books.assert_called_once()

    @patch("builtins.input", side_effect=["5", "1", "выдана", "6"])
    @patch("builtins.print")
    def test_update_status_command(self, mock_print, mock_input):
        """Тест команды обновления статуса."""
        self.library.update_status.return_value = True
        self.cli.run()
        self.library.update_status.assert_called_once_with(1, "выдана")
