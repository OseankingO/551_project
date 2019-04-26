import unittest
from wow import db
from wow.model import User
from woo.users import routes


class TestUser(unittest.TestCase):
    def test_users(self):
        user = User(username="Sam", email="Sam@qq.com", password="123")
        db.session.add(user)
        db.session.commit()
