import json
import logging
from abc import ABC

from domain.user.factory import UserFactory
from domain.user.persistence_interface import UserPersistenceInterface
from domain.user.user import User


class UserPersistenceFile(UserPersistenceInterface):
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def get_all(self) -> list[User]:
        try:
            # TODO refactor with -done
            with open(self.__file_path) as file:
                contents = file.read()
            users_info = json.loads(contents)
            factory = UserFactory()
            return [factory.make_from_persistance(x) for x in users_info]
        except Exception as e:
            # TODO Homework, log error -done
            logging.error("Failed to load users!}" + str(e))

    def add(self, user: User):
        current_users = self.get_all()
        current_users.append(user)
        users_info = [(str(x.id), x.username, x.stocks) for x in current_users]
        users_json = json.dumps(users_info)
        # TODO Homework refactor with -done
        with open(self.__file_path, "w") as file:
            file.write(users_json)
