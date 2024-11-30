import db # Модуль работы с БД. 
import seed # Заполнение рыбой
import queries # Запросы для проверки
import create_tables as ct # Создаем таблицы

if __name__ == "__main__":
    """
    Для проверки ДЗ:
    1. Отркыть консоль и перейти в директорию 'bash cd task_1'
    2. Запускаем контейнер 'bash docker-compose up -d' в тихом режиме. БД будет создана автоматом
    3. main.py просто запускаем и дз выполняется.
    """
    ct.create_tables(db)
    seed.fill_tables(db) # Достаточно запустить 1-2 раза для заполнения базы
    queries.do_all(db) # Выполнить все запросы из задания.

