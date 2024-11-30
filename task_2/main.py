from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from pymongo import errors

#  Connection
uri = "mongodb+srv://goitlearn:zxtOSgBQ63o0bPUh@cluster0.zjc5v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server with ignored SSL verification
client = MongoClient(uri, server_api=ServerApi('1'), tls=True, tlsAllowInvalidCertificates=True)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Ошибка подключения: {e}")

db = client.book
collection = db['cats']

# Функции CRUD

# CREATE INITIAL
def create_initial_cats():
    """ Заполняем БД рыбой """
    try:
        result_many = collection.insert_many(
            [
                {
                    "name": "barsik",
                    "age": 3,
                    "features": ["ходить в капці", "дає себе гладити", "рудий"],
                },
                {
                    "name": "Lama",
                    "age": 2,
                    "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
                },
                {
                    "name": "Liza",
                    "age": 4,
                    "features": ["ходить в лоток", "дає себе гладити", "білий"],
                },
            ]
        )
        print(f"Добавленные документы: {result_many.inserted_ids}")
    except errors.PyMongoError as e:
        print(f"Ошибка при добавлении: {e}")

# CREATE
def create_cat():
    """ Создать нового кота """
    name = input("Введите имя кота: ")
    age = int(input("Возраст кота: "))
    features = input("Введите характеритстики через запятую: ").split(", ")
    try:
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        collection.insert_one(cat)
        print(f"Кот '{name}' успешно добавлен.")
    except errors.PyMongoError as e:
        print(f"Ошибка при добавлении: {e}")


# READ
def read_all_cats():
    """ Прочитать все документы коллекции """
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except errors.PyMongoError as e:
        print(f"Ошибка при чтении данных: {e}")

def read_cat_by_name():
    """ Вывод информации по имени кота """
    name = input("Введите имя кота: ")
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кот с таким именем '{name}' не найден.")
    except errors.PyMongoError as e:
        print(f"Ошибка при поиске: {e}")

# UPDATE
def update_cat_age():
    """ Обновить возраст по имени """
    name = input("Введите имя кота: ")
    new_age = int(input("Введите новый возраст: "))
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print(f"Возраст кота '{name}' изменен на -> {new_age}.")
        else:
            print(f"Кот '{name}' не найден.")
    except errors.PyMongoError as e:
        print(f"Ошибка при обновлении возраста: {e}")

def add_feature_to_cat():
    """ Добавить новую характеристику по имени """
    name = input("Введите имя кота: ")
    new_feature = input("Введите новую характеристику: ")
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.matched_count > 0:
            print(f"Характеристика '{new_feature}' добавлена коту '{name}'.")
        else:
            print(f"Кот '{name}' не найден.")
    except errors.PyMongoError as e:
        print(f"Ошибка при добавлении характеристики: {e}")

# DELETE
def delete_cat_by_name():
    """ Удалить кота по имени """
    name = input("Введите имя кота: ")
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кот '{name}' удален.")
        else:
            print(f"Кот '{name}' не найден.")
    except errors.PyMongoError as e:
        print(f"Ошибка при удалении кота: {e}")

def delete_all_cats():
    """ Удалить все записи """
    try:
        result = collection.delete_many({})
        print(f"Удалено {result.deleted_count} записей.")
    except errors.PyMongoError as e:
        print(f"Ошибка при дуалении всех записей: {e}")

# Основной цикл
if __name__ == "__main__":
    create_initial_cats()  # Забъем базу рыбой
    while True:
        print("\nВыберите операцию:")
        print("1. Создать кота")
        print("2. Вывести все запси")
        print("3. Вывести запись по имени")
        print("4. Обновить возраст по имени")
        print("5. Добавить характеристику")
        print("6. Удалить кота по имени")
        print("7. Удалить все записи")
        print("8. Выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            create_cat()

        elif choice == "2":
            read_all_cats()

        elif choice == "3":
            read_cat_by_name()

        elif choice == "4":
            update_cat_age()

        elif choice == "5":
            add_feature_to_cat()

        elif choice == "6":
            delete_cat_by_name()

        elif choice == "7":
            delete_all_cats()

        elif choice == "8":
            print("Всего доброго!")
            break

        else:
            print("Ошибка, сделайте выбор еще раз.")