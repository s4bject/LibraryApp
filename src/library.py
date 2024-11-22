from models.models import Book


class Library:
    """Класс библиотеки для управления книгами."""

    def __init__(self, persistence):
        self.persistence = persistence
        self.books = self.__load_books()

    def __load_books(self):
        """Загружает книги из хранилища с обработкой ошибок."""
        try:
            data = self.persistence.load()
            return [Book(**book) for book in data]
        except Exception as e:
            print(f"Ошибка загрузки книг: {e}")
            return []

    def __save_books(self):
        """Сохраняет книги в хранилище с обработкой ошибок."""
        try:
            data = [book.__dict__ for book in self.books]
            self.persistence.save(data)
        except Exception as e:
            print(f"Ошибка сохранения книг: {e}")

    def add_book(self, title, author, year):
        """Добавляет книгу в библиотеку с обработкой ошибок."""
        try:
            new_id = max((book.id for book in self.books), default=0) + 1
            new_book = Book(new_id, title, author, year)
            self.books.append(new_book)
            self.__save_books()
        except Exception as e:
            print(f"Ошибка добавления книги: {e}")

    def delete_book(self, book_id):
        """Удаляет книгу по ID с обработкой ошибок."""
        try:
            book = self.find_book_by_id(book_id)
            if book:
                self.books.remove(book)
                self.__save_books()
                return True
            else:
                return False
        except Exception as e:
            print(f"Ошибка удаления книги: {e}")

    def find_book_by_id(self, book_id):
        """Ищет книгу по ID с обработкой ошибок."""
        try:
            for book in self.books:
                if book.id == book_id:
                    return book
            return None
        except Exception as e:
            print(f"Ошибка поиска книги по ID: {e}")
            return None

    def search_books(self, query, field):
        """Ищет книги по заданному полю с обработкой ошибок."""
        try:
            return [book for book in self.books if query.lower() in str(getattr(book, field)).lower()]
        except ValueError as ve:
            print(f"Ошибка валидации: {ve}")
            return []
        except Exception as e:
            print(f"Ошибка поиска книг: {e}")
            return []

    def update_status(self, book_id, new_status):
        """Изменяет статус книги с обработкой ошибок."""
        try:
            book = self.find_book_by_id(book_id)
            if book:
                book.status = new_status
                self.__save_books()
                return True
            else:
                return False
        except Exception as e:
            print(f"Ошибка обновления статуса книги: {e}")

    def display_books(self, books=None):
        """Отображает список книг с обработкой ошибок."""
        try:
            books = books if books is not None else self.books
            if not books:
                return None
            for book in books:
                print(book)
        except Exception as e:
            print(f"Ошибка отображения книг: {e}")
