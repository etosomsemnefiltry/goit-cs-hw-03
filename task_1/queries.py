
def get_all_user_tasks(conn):
    """ Отримати всі завдання певного користувача """
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM tasks WHERE user_id = (SELECT id FROM users ORDER BY RANDOM() LIMIT 1)"
            cursor.execute(query)
            results = cursor.fetchall()
            print("\nОтримати всі завдання певного користувача:\n")
            print(f"{query} \n")
            for res in results:
                print(f"{res}\n") 
    except Exception as e:
        print(f"Ошибка запроса {e}")

def get_tasks_with_certain_id(conn, status_id=1):
    """ Вибрати завдання за певним статусом """
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM tasks WHERE status_id = %s"
            cursor.execute(query, (status_id,))
            results = cursor.fetchall()
            print("\n\nВибрати завдання за певним статусом:\n")
            print(f"{query} \n")
            for res in results:
                print(f"{res}\n") 
    except Exception as e:
        print(f"Ошибка запроса {e}")

def update_task(conn, id=1):
    """ Оновити статус конкретного завдання """
    try:
        with conn.cursor() as cursor:
            query = "UPDATE tasks SET status_id = 2 WHERE id = %s"
            cursor.execute(query, (id,))
            conn.commit()
            print("\n\nОновити статус конкретного завдання:\n")
            print(f"{query} \n")
            print(f"Задача с ID {id} была обновлена до статуса status_id = 2.\n") 
    except Exception as e:
        print(f"Ошибка запроса {e}")

def get_users_with_no_tasks(conn):
    """ Отримати список користувачів, які не мають жодного завдання """
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks)"
            cursor.execute(query)
            results = cursor.fetchall()
            print("\n\nОтримати список користувачів, які не мають жодного завдання:\n")
            print(f"{query} \n")
            for res in results:
                print(f"{res}") 
    except Exception as e:
        print(f"Ошибка запроса {e}")

def insert_task(conn, user_id=1, title="", description="", status_id=1):
    """ Додати нове завдання для конкретного користувача """
    title = "Test task add"
    description="Lorem ipsum"
    try:
        with conn.cursor() as cursor:
            query = "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (title, description, status_id, user_id,))
            conn.commit()
            print("\n\nДодати нове завдання для конкретного користувача:\n")
            print(f"{query} \n")
            print(f"Задача добавлена.\n") 
    except Exception as e:
        print(f"Ошибка запроса {e}")

def get_not_finished_tasks(conn):
    """ Отримати всі завдання, які ще не завершено """
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM tasks WHERE status_id != 3"
            cursor.execute(query)
            results = cursor.fetchall()
            print("\n\nОтримати всі завдання, які ще не завершено:\n")
            print(f"{query} \n")
            for res in results:
                print(f"{res}") 
    except Exception as e:
        print(f"Ошибка запроса {e}")

def delete_task(conn, id=1):
    """ Видалити конкретне завдання """
    try:
        with conn.cursor() as cursor:
            query = "DELETE FROM tasks WHERE id = %s"
            cursor.execute(query, (id,))
            conn.commit()
            print("\n\nВидалити конкретне завдання:\n")
            print(f"{query} \n")
            print(f"Задача {id} удалена.\n") 
    except Exception as e:
        print(f"Ошибка запроса {e}")

def get_user_by_email(conn, email):
    """ Знайти користувачів з певною електронною поштою """
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM users WHERE email LIKE %s LIMIT 1"
            cursor.execute(query, (f"%{email}%",))
            results = cursor.fetchall()
            print("\n\nЗнайти користувачів з певною електронною поштою:\n")
            print(f"{query} \n")
            for res in results:
                print(f"{res}") 
    except Exception as e:
        print(f"Ошибка запроса {e}")

def update_user(conn, id=1, name="VASYA"):
    """ Оновити ім'я користувача """
    try:
        with conn.cursor() as cursor:
            query = "UPDATE users SET fullname = %s WHERE id = %s"
            cursor.execute(query, (name, id,))
            conn.commit()
            print("\n\nОновити ім'я користувача:\n")
            print(f"{query} \n")
            print(f"Пользователь {id} теперь носит имя {name}.\n") 
    except Exception as e:
        print(f"Ошибка запроса {e}")
    
def count_tasks_by_status(conn):
    """ Отримати кількість завдань для кожного статусу """
    try:
        with conn.cursor() as cursor:
            query = "SELECT s.name AS status_name, COUNT(t.id) AS task_count FROM tasks t JOIN status s ON t.status_id = s.id GROUP BY s.name"
            cursor.execute(query)
            results = cursor.fetchall()
            print("\n\nОтримати кількість завдань для кожного статусу:\n")
            print(f"{query} \n")
            for status_name, task_count in results:
                print(f"Статус: {status_name}, Кол-во заданий: {task_count}")
   
    except Exception as e:
        print(f"Ошибка запроса {e}")

def get_tasks_by_email_domain(conn, domain="example.com"):
    """ Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти """
    try:
        with conn.cursor() as cursor:
            query = "SELECT t.* FROM tasks t JOIN users u ON t.user_id = u.id WHERE u.email LIKE %s"
            cursor.execute(query, (f"%{domain}",))
            results = cursor.fetchall()
            print("\n\nОтримати завдання, які призначені користувачам з певною доменною частиною електронної пошти:\n")
            print(f"{query} \n")
            if results:
                for res in results:
                    print(res)
            else:
                print(f"Нет заданий для пользователей с доменом почты '{domain}'.")
   
    except Exception as e:
        print(f"Ошибка запроса {e}")

def get_tasks_with_empty_description(conn):
    """ Отримати список завдань, що не мають опису """
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM tasks WHERE description IS NULL"
            cursor.execute(query)
            results = cursor.fetchall()
            print("\n\nОтримати список завдань, що не мають опису:\n")
            print(f"{query} \n")
            if results:
                for res in results:
                    print(res)
            else:
                print(f"Нет заданий с пустым описанием.")
   
    except Exception as e:
        print(f"Ошибка запроса {e}")

def get_tasks_with_empty_description(conn):
    """ Вибрати користувачів та їхні завдання, які є у статусі 'in progress' """
    try:
        with conn.cursor() as cursor:
            query = """
            SELECT u.*, t.* 
            FROM users as u
            INNER JOIN tasks as t ON t.user_id = u.id 
            WHERE t.status_id = 2
            """
            cursor.execute(query)
            results = cursor.fetchall()
            print("\n\nВибрати користувачів та їхні завдання, які є у статусі 'in progress':\n")
            print(f"{query} \n")
            if results:
                for res in results:
                    print(res)
            else:
                print(f"Нет заданий с нужными параметрами.")
   
    except Exception as e:
        print(f"Ошибка запроса {e}")

def get_users_and_count_tasks(conn):
    """ Отримати користувачів та кількість їхніх завдань """
    try:
        with conn.cursor() as cursor:
            query = """
            SELECT u.id AS user_id, u.fullname, COUNT(t.id) AS task_count
            FROM users AS u
            LEFT JOIN tasks AS t ON u.id = t.user_id
            GROUP BY u.id
            """
            cursor.execute(query)
            results = cursor.fetchall()
            print("\n\nОтримати користувачів та кількість їхніх завдань:\n")
            print(f"{query} \n")
            for res in results:
                print(res)
   
    except Exception as e:
        print(f"Ошибка запроса {e}")

def do_all(db):
    conn = db.get_db()
    try:
        get_all_user_tasks(conn)
        get_tasks_with_certain_id(conn, 2)
        update_task(conn, 1)
        get_users_with_no_tasks(conn)
        insert_task(conn)
        get_not_finished_tasks(conn)
        delete_task(conn, id=59)
        get_user_by_email(conn, "arthur78@example.com")
        update_user(conn, 1, "SUPERMAN")
        count_tasks_by_status(conn)
        get_tasks_by_email_domain(conn, "example.com")
        get_tasks_with_empty_description(conn)
        get_users_and_count_tasks(conn)
        print("\nЕсли это сообщение видно, значит БД создана, таблицы забиты информацией, все запросы выполнены.")
    finally:
        if conn:
            conn.close()