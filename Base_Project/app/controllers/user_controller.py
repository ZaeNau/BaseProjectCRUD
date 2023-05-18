from app.models.user import User

class UserController:
    def __init__(self):
        self.users = []

    def create_user(self, username, email):
        user_id = len(self.users) + 1
        user = User(user_id, username, email)
        self.users.append(user)
        return user

    def get_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def update_user(self, user_id, new_username, new_email):
        user = self.get_user(user_id)
        if user:
            user.username = new_username
            user.email = new_email
            return user
        return None

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        if user:
            self.users.remove(user)
            return True
        return False

    def get_all_users(self):
        return self.users
