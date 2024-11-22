from abc import ABC, abstractmethod
import json


class Persistence(ABC):
    """Абстракция для работы с хранилищем. Позволяет добавить новый метод хранения книг, никак не изменяя весь остальной код"""

    @abstractmethod
    def load(self):
        """Загружает данные из хранилища."""
        pass

    @abstractmethod
    def save(self, books):
        """Сохраняет данные в хранилище."""
        pass


class JSONPersistence(Persistence):
    """Реализация хранилища на основе JSON-файла."""

    def __init__(self, storage_file="library.json"):
        self.storage_file = storage_file

    def load(self):
        """Загружает данные из JSON с обработкой исключений."""
        try:
            with open(self.storage_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            """Если файл не найден."""
            print(f"Файл {self.storage_file} не найден. Возвращаю пустой список.")
            return []
        except json.JSONDecodeError as e:
            """Ошибка при парсинге JSON."""
            print(f"Ошибка чтения JSON из файла {self.storage_file}: {e}")
            return []
        except Exception as e:
            """Обработка любых других ошибок."""
            print(f"Неожиданная ошибка при загрузке данных: {e}")
            return []

    def save(self, books):
        """Сохраняет данные в JSON с обработкой исключений."""
        try:
            with open(self.storage_file, "w", encoding="utf-8") as file:
                json.dump(books, file, ensure_ascii=False, indent=4)
        except TypeError as e:
            """Ошибка сериализации."""
            print(f"Ошибка сериализации данных: {e}")
        except IOError as e:
            """Ошибка записи в файл."""
            print(f"Ошибка записи данных в файл {self.storage_file}: {e}")
        except Exception as e:
            """Обработка любых других ошибок."""
            print(f"Неожиданная ошибка при сохранении данных: {e}")
