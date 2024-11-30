import pg8000

# Инициация подключения к БД

def get_db():
    try:
        return pg8000.connect(
                user="pavel", 
                password="1234qwer", 
                database="newdb", 
                host="localhost"
                )
    except Exception as e:
        print(f"Ошибка подключения в базе данных: {e}")
