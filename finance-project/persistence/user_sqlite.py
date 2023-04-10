import sqlite3

from domain.user.factory import UserFactory
from domain.user.persistence_interface import UserPersistenceInterface
from domain.user.user import User


class UserPersistenceSqlite(UserPersistenceInterface):
    def get_all(self) -> list[User]:
        try:
            with sqlite3.connect("main_users.db") as conn:
                cursor = conn.cursor()
                # TODO homework, try except return empty list if no db -done
                cursor.execute("SELECT * FROM users")
                users_info = cursor.fetchall()
        except sqlite3.OperationalError as e:
            if "no such table" in str(e):
                return []
            else:
                raise e
        factory = UserFactory()
        users = [factory.make_from_persistance(x) for x in users_info]
        return users

    def add(self, user: User):
        with sqlite3.connect("main_users.db") as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(f"INSERT INTO users(id, username) VALUES ('{user.id}','{user.username}')")
            except sqlite3.OperationalError as e:
                if "no such table" in str(e):
                    cursor.execute("CREATE TABLE users (id TEXT PRIMARY KEY, username TEXT NOT NULL)")
                else:
                    raise e
                cursor.execute(f"INSERT INTO users(id, username) VALUES ('{user.id}','{user.username}')")
            conn.commit()

    def delete(self, uuid: int):
        with sqlite3.connect("main_users.db") as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM users WHERE id = {uuid}")
            conn.commit()

    def edit(self, user: User):
        with sqlite3.connect("main_users.db") as conn:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE users SET username = '{user.username}' where id = '{user.id}'")
            conn.commit()
