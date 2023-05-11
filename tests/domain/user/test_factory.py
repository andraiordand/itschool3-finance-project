import unittest

from domain.user.factory import UserFactory, InvalidUsername
from domain.user.user import User


class UserFactoryTestCase(unittest.TestCase):
    def test_it_creates_user_if_the_username_is_between_6_and_20_chars(self):
        username = "between-6-and-20"

        factory = UserFactory()

        actual_user = factory.make_new(username)

        self.assertEqual(username, actual_user.username)
        self.assertEqual(User, type(actual_user))

    def test_it_raises_exception_if_the_username_is_below_6_chars(self):
        username = "Below"
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)

        self.assertEqual(
            "Username should have at least 6 characters!", str(context.exception)
        )

    # ("TODO")- done
    def test_it_raises_exception_if_the_username_is_above_20_chars(self):
        username = "Username-is-above-20-characters"
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)

        self.assertEqual(
            "Username should not have more than 20 characters!", str(context.exception)
        )

    # ("TODO")- done
    def test_it_creates_a_user_if_the_username_has_valid_chars(self):
        username = "Valid-username-123"

        factory = UserFactory()

        actual_user = factory.make_new(username)

        self.assertEqual(username, actual_user.username)
        self.assertEqual(User, type(actual_user))

    # ("TODO")- done
    def test_it_raises_exception_if_the_username_has_invalid_chars(self):
        username = "Invalid-username-123#"
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)

        self.assertEqual(
            "Username contains invalid characters!", str(context.exception)
        )


if __name__ == "__main__":
    unittest.main()
