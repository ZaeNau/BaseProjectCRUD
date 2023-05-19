class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.roles = [] #untuk menyimpan roles

    def assign_role(self, role):
        self.roles.append(role)
