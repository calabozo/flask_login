from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, user: dict):
        self.username = user['name']
        self.pwd = user['password']
        self.user_id = user['id']

    def __repr__(self):
        return '<User %r>' % self.username

    def get_id(self):
        return self.user_id

    @staticmethod
    def get_user_from_name(name):
        from dataweb.user_list import fetch_user
        user = fetch_user(property='name', value=name)
        if user is not None:
            return User(user)
        else:
            return None

    @staticmethod
    def get_user_from_id(user_id):
        from dataweb.user_list import fetch_user
        user = fetch_user(property='id', value=user_id)
        if user is not None:
            return User(user)
        else:
            return None
