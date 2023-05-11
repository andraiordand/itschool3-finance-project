import unittest
import uuid
from uuid import uuid4

from domain.user.user import User


class UserTestCase(unittest.TestCase):
    def test_user_sets_the_right_username(self):
        # set up
        username = "random_generated"
        uuid = uuid4()
        user = User(username=username, uuid=uuid)
        # execution
        actual_username = user.username
        actual_uuid = user.uuid
        # assertion
        self.assertEqual(username, actual_username)
        self.assertEqual(uuid, actual_uuid)

    def test_it_sets_empty_list_if_we_do_not_specify_stock(self):
        user = User("random_username")

        actual_stocks = user.stocks

        self.assertEqual([], actual_stocks)

    @unittest.skip("TODO: Homework")
    def test_it_sets_the_stocks_we_give(self):
        # sets a list of 3 strings
        user = User("random_username", stocks=["TSLA", "NVDA", "RBLX"])

        actual_stocks = user.stocks
        expected_stocks = ["TSLA", "NVDA", "RBLX"]

        self.assertEqual(user.stocks, expected_stocks)


if __name__ == "__main__":
    unittest.main()
