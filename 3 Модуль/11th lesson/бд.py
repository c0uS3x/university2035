import sqlite3


class User:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender


def create_table_users(date_base):
    command = """
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        gender TEXT
        );
    """
    date_base.execute(command)


def add_user(data_base, user):
    command = """
        INSERT INTO users (name, surname, gender)
        VALUES (?, ?, ?)
    """
    data_base.execute(command, (user.name, user.surname, user.gender))


def get_user_list(date_base):
    command = """
        SELECT * FROM Users
    """

    # result = date_base.execute(command)
    # print(list(result))


def get_men_list(date_base):
    command = """
        SELECT * FROM Users
        WHERE gender="Мужчина"
    """

    result = date_base.execute(command)
    print(list(result))

def get_women_list(date_base):
    command = """
        SELECT * FROM Users
        WHERE gender="Женщина"
    """

    result = date_base.execute(command)
    print(list(result))


def delete_users(date_base, user_id, name):
    command = """
        DELETE FROM users
        WHERE id = ? and name = ?
    """

    date_base.execute(command, (user_id, name))


def update_user(date_base, name, user_id):
    command = """
        UPDATE users
        SET name = ?
        WHERE id = ?
    """

    date_base.execute(command, (name, user_id))


with sqlite3.connect('data.db') as date_base:
    create_table_users(date_base)
    # add_user(date_base, User('Иван', "Иванов", "Мужчина"))
    get_user_list(date_base)
    delete_users(date_base, 4, 'Иван')
    update_user(date_base, "Димон", 3)
    get_men_list(date_base)
    get_women_list(date_base)