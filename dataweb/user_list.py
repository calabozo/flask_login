users = [
    {'id': 1, 'name': 'admin', 'password': 'a1234'},
    {'id': 2, 'name': 'alice', 'password': 'alice1'},
    {'id': 3, 'name': 'bob', 'password': 'bob_pwd'},
]


def fetch_user(property: str, value: str):
    user = [user for user in users if user[property] == value]
    if len(user) > 0:
        return user[0]
    else:
        return None
