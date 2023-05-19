from app.models.role import Role

class RoleController:
    def __init__(self):
        self.roles = []

    def create_role(self, name, description):
        role_id = len(self.roles) + 1
        role = Role(role_id, name, description)
        self.roles.append(role)
        return role

    def get_role(self, role_id):
        for role in self.roles:
            if role.role_id == role_id:
                return role
        return None

    def update_role(self, role_id, new_name, new_description):
        role = self.get_role(role_id)
        if role:
            role.name = new_name
            role.description = new_description
            return role
        return None

    def delete_role(self, role_id):
        role = self.get_role(role_id)
        if role:
            self.roles.remove(role)
            return True
        return False

    def get_all_roles(self):
        return self.roles
    
    def assign_permission_to_role(self, role_id, permission):
        role = self.get_role(role_id)
        if role:
            role.assign_permission(permission)
            return True
        return False