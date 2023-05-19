class Role:
    def __init__(self, role_id, name, description):
        self.role_id = role_id
        self.name = name
        self.description = description
        self.permissions = [] #untuk menyimpan daftar izin

    def assign_permission(self, permission):
        self.assign_permission.append(permission)