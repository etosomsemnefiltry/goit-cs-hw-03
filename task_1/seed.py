from faker import Faker

fake = Faker()    

def fill_users_table(conn, rand_records = 15):
    try:
        cursor = conn.cursor()
        for _ in range(rand_records):
            fullname = fake.name()
            email = fake.unique.email()
            cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
        conn.commit()
        print(f"Сгенерировано {rand_records} записей в таблицу users.")
    except Exception as e:
        print(f"Ошибка при заполнении таблицы users: {e}")
    finally:
        if cursor:
            cursor.close()

def fill_status_table(conn):
    try:
        cursor = conn.cursor()
        statuses = [('new',), ('in progress',), ('completed',)]
        for status in statuses:
            cursor.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT DO NOTHING", (status,))
        print(f"Таблица статусов заполнена.")
        conn.commit()
    except Exception as e:
        print(f"Ошибка при заполнении таблицы status: {e}")
    finally:
        if cursor:
            cursor.close()

def fill_tasks_table(conn, rand_records=25):
    try:
        cursor = conn.cursor()
        for _ in range(rand_records):
            title = fake.sentence(nb_words=5)
            description = fake.text(max_nb_chars=200)
            cursor.execute("SELECT id FROM status ORDER BY RANDOM() LIMIT 1")
            status_id = cursor.fetchone()[0]
            cursor.execute("SELECT id FROM users ORDER BY RANDOM() LIMIT 1")
            user_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                           (title, description, status_id, user_id))
        conn.commit()
        print(f"Добавлено {rand_records} записей в таблицу tasks.")
    except Exception as e:
        print(f"Ошибка при заполнении таблицы tasks: {e}")
    finally:
        if cursor:
            cursor.close()


def fill_tables(db):
    conn = db.get_db()
    try:
        fill_users_table(conn)
        fill_status_table(conn)
        fill_tasks_table(conn)
    except Exception as e:
        print(f"Ошибка при заполнении таблиц: {e}")
    finally:
        if conn:
            conn.close()

