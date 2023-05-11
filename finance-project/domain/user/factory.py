import string
import uuid
from domain.user.user import User


class InvalidUsername(Exception):
    pass


class UserFactory:
    def make_new(self, username: str) -> User:
        # TODO - done
        if len(username) < 6:
            raise InvalidUsername("Username should have at least 6 characters!")
        if len(username) > 20:
            raise InvalidUsername("Username should not have more than 20 characters!")
        valid_chars = set(string.digits + string.ascii_letters + "-")
        valid_chars = {char for char in username if char in valid_chars}
        if set(username) != valid_chars:
            raise InvalidUsername("Username contains invalid characters!")
        user_uuid = uuid.uuid4()
        return User(user_uuid, username)

    def make_from_persitance(self, info: tuple) -> User:
        return User(
            uuid=uuid.UUID(info[0]),
            username=info[1],
        )
