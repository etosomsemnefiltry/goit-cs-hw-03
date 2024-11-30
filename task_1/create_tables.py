
def create_users_table():
    return """ 
    CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL
    );
    """

def create_status_table():
    return """
    CREATE TABLE IF NOT EXISTS status(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
    )
    """

def create_tasks_table():
    return """
    CREATE TABLE IF NOT EXISTS tasks(
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES status(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """
    
def create_tables(db):
    conn = db.get_db()
    cursor = conn.cursor()
    try:
        
        cursor.execute(create_users_table())
        print(f"Таблица users создана.")

        cursor.execute(create_status_table())
        print(f"Таблица status создана.")

        cursor.execute(create_tasks_table())
        print(f"Таблица status создана.")

        conn.commit()

    except Exception as e:
        print(f"Ошибка запроса к базе данных: {e}")
        conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()