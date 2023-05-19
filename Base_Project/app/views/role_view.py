from app.controllers.role_controller import RoleController

class RoleView:
    def __init__(self):
        self.role_controller = RoleController()

    def create_role(self):
        name = input("Enter role name: ")
        description = input("Enter role description: ")
        role = self.role_controller.create_role(name, description)
        print("Role created successfully.")
        self.display_role(role)

    def display_role(self, role):
        print(f"Role ID: {role.role_id}")
        print(f"Name: {role.name}")
        print(f"Description: {role.description}")

    def update_role(self):
        role_id = int(input("Enter role ID to update: "))
        new_name = input("Enter new role name: ")
        new_description = input("Enter new role description: ")
        updated_role = self.role_controller.update_role(role_id, new_name, new_description)
        if updated_role:
            print("Role updated successfully.")
            self.display_role(updated_role)
        else:
            print("Role not found.")

    def delete_role(self):
        role_id = int(input("Enter role ID to delete: "))
        if self.role_controller.delete_role(role_id):
            print("Role deleted successfully.")
        else:
            print("Role not found.")

    def display_all_roles(self):
        roles = self.role_controller.get_all_roles()
        if roles:
            print("All Roles:")
            for role in roles:
                self.display_role(role)
                print("-------------------")
        else:
            print("No roles found.")

    def menu(self):
        while True:
            print("\nRole Management Menu:")
            print("1. Create Role")
            print("2. Update Role")
            print("3. Delete Role")
            print("4. View All Roles")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                self.create_role()
            elif choice == "2":
                self.update_role()
            elif choice == "3":
                self.delete_role()
            elif choice == "4":
                self.display_all_roles()
            elif choice == "5":
                print("Exiting Role Management...")
                break
            else:
                print("Invalid choice. Please try again.")

# Usage example:
if __name__ == "__main__":
    role_view = RoleView()
    role_view.menu()
