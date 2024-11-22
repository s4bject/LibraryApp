from src.library import Library


class LibraryCLI:
    """Интерфейс командной строки."""

    def __init__(self, library):
        """
        Инициализирует CLI с объектом библиотеки.
        :param library: Объект класса Library.
        """
        self.library = library

    def run(self):
        """Запуск CLI."""
        while True:
            print("\nДоступные команды:")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Найти книгу")
            print("4. Отобразить все книги")
            print("5. Изменить статус книги")
            print("6. Выйти")

            command = input("Введите номер команды: ").strip()

            try:
                if command == "1":
                    title = input("Введите название книги: ").strip()
                    author = input("Введите автора книги: ").strip()
                    year = input("Введите год издания: ").strip()
                    if year:
                        if not year.isdigit():
                            raise ValueError("Год издания должен быть числом.")
                        year = int(year)
                    self.library.add_book(title, author, year)
                    print("Книга успешно добавлена.")

                elif command == "2":
                    book_id_input = input("Введите ID книги для удаления: ").strip()
                    if not book_id_input.isdigit():
                        raise ValueError("ID книги должен быть числом.")
                    book_id = int(book_id_input)
                    if self.library.delete_book(book_id):
                        print("Книга успешно удалена.")
                    else:
                        print("Книга с таким ID не существует.")

                elif command == "3":
                    field = input("По какому полю искать? (title, author, year): ").strip()
                    if field not in ["title", "author", "year"]:
                        raise ValueError("Недопустимое поле для поиска.")
                    query = input(f"Введите значение для поиска по {field}: ").strip()
                    results = self.library.search_books(query, field)
                    if results:
                        print("Найденные книги:")
                        self.library.display_books(results)
                    else:
                        print("Книги не найдены.")

                elif command == "4":
                    print('Книги в библиотеке:')
                    books = self.library.display_books()

                elif command == "5":
                    book_id_input = input("Введите ID книги: ").strip()
                    if not book_id_input.isdigit():
                        raise ValueError("ID книги должен быть числом.")
                    book_id = int(book_id_input)
                    new_status = input("Введите новый статус ('в наличии' или 'выдана'): ").strip()
                    if new_status not in ["в наличии", "выдана"]:
                        raise ValueError("Недопустимый статус. Используйте 'в наличии' или 'выдана'.")
                    if self.library.update_status(book_id, new_status):
                        print("Статус книги успешно обновлен.")
                    else:
                        print("Книга с таким ID не найдена.")

                elif command == "6":
                    print("Выход из программы.")
                    break

                else:
                    print("Недопустимая команда. Попробуйте снова.")
            except ValueError as ve:
                print(f"Ошибка ввода: {ve}")
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")
