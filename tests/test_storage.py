import unittest
import os
from src.storage import JSONPersistence

class TestJSONPersistence(unittest.TestCase):

    def setUp(self):
        """Подготовка временного файла для тестов."""
        self.test_file = "tests/test_library.json"
        self.persistence = JSONPersistence(self.test_file)

    def tearDown(self):
        """Удаление временного файла после тестов."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load(self):
        """Тест сохранения и загрузки данных."""
        data = [{"id": 1, "title": "Test Book", "author": "Author", "year": 2024}]
        self.persistence.save(data)
        loaded_data = self.persistence.load()
        self.assertEqual(data, loaded_data)

    def test_load_file_not_found(self):
        """Тест загрузки, если файл отсутствует."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.assertEqual(self.persistence.load(), [])

    def test_load_invalid_json(self):
        """Тест загрузки, если JSON-файл поврежден."""
        with open(self.test_file, "w") as file:
            file.write("{ invalid json }")
        self.assertEqual(self.persistence.load(), [])
