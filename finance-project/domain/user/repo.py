import json
import uuid
from singleton import singleton
from domain.asset.repo import AssetRepo
from domain.user.factory import UserFactory
from domain.user.persistence_interface import UserPersistenceInterface
from domain.user.user import User


@singleton
class UserRepo:
    def __init__(self, persistence: UserPersistenceInterface):
        print("Init user repo")
        self.__persistence = persistence
        self.__users = None

    def add(self, new_user: User):
        # TODO homework, refactor to not have duplicate code + add for get_by_id -done
        self.__verify_if_there_are_users()
        self.__persistence.add(new_user)
        self.__users.append(new_user)

    def get_all(self) -> list[User]:
        self.__verify_if_there_are_users()
        return self.__users

    def get_by_id(self, uid: str) -> User:
        self.__verify_if_there_are_users()
        for u in self.__users:
            if u.id == uuid.UUID(hex=uid):
                assets = AssetRepo().get_for_user(u)
                return User(
                    uuid=u.id,
                    username=u.username,
                    stocks=assets
                )

    def delete_by_id(self, user_id: User.id):
        self.__verify_if_there_are_users()
        for u in self.__users:
            if user_id == u.id:
                self.__users.remove(u)
        self.__users = None
        self.__verify_if_there_are_users()

    def edit_by_id(self, user_id: User.id, username: str):
        self.__verify_if_there_are_users()
        for u in self.users:
            if user_id == u.id:
                u.username = username
        self.persistence.edit_by_id(user_id, username)
        self.__users = None
        self.__check_we_have_users()

    def __verify_if_there_are_users(self):
        if self.__users is None:
            self.__users = self.__persistence.get_all()


