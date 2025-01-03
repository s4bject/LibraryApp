class Book:
    """Модель книги."""

    def __init__(self, id, title=None, author=None, year=None, status="в наличии"):
        """
        Инициализирует объект книги.
        :param id: Уникальный идентификатор книги.
        :param title: Название книги (по умолчанию: "У книги нет названия").
        :param author: Автор книги (по умолчанию: "У книги нет автора").
        :param year: Год издания (по умолчанию: "У книги неизвестен год выпуска").
        :param status: Статус книги (по умолчанию: "в наличии").
        """
        self.id = id
        self.title = title or "У книги нет названия"
        self.author = author or "У книги нет автора"
        self.year = year or "У книги неизвестен год выпуска"
        self.status = status

    def __str__(self):
        """
        Возвращает строковое представление книги.
        """
        return (f"ID: {self.id}, Название: {self.title}, Автор: {self.author}, "
                f"Год: {self.year}, Статус: {self.status}")
