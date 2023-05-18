from app.controllers.user_controller import UserController

class UserView:
    def __init__(self):
        self.user_controller = UserController()

    def create_user(self):
        username = input("Enter username: ")
        email = input("Enter email: ")
        user = self.user_controller.create_user(username, email)
        print("User created successfully.")
        self.display_user(user)

    def display_user(self, user):
        print(f"User ID: {user.user_id}")
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")

    def update_user(self):
        user_id = int(input("Enter user ID to update: "))
        new_username = input("Enter new username: ")
        new_email = input("Enter new email: ")
        updated_user = self.user_controller.update_user(user_id, new_username, new_email)
        if updated_user:
            print("User updated successfully.")
            self.display_user(updated_user)
        else:
            print("User not found.")

    def delete_user(self):
        user_id = int(input("Enter user ID to delete: "))
        if self.user_controller.delete_user(user_id):
            print("User deleted successfully.")
        else:
            print("User not found.")

    def display_all_users(self):
        users = self.user_controller.get_all_users()
        if users:
            print("All Users:")
            for user in users:
                self.display_user(user)
                print("-------------------")
        else:
            print("No users found.")

    def menu(self):
        while True:
            print("\nUser Management Menu:")
            print("1. Create User")
            print("2. Update User")
            print("3. Delete User")
            print("4. View All Users")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                self.create_user()
            elif choice == "2":
                self.update_user()
            elif choice == "3":
                self.delete_user()
            elif choice == "4":
                self.display_all_users()
            elif choice == "5":
                print("Exiting User Management...")
                break
            else:
                print("Invalid choice. Please try again.")

# Usage example:
if __name__ == "__main__":
    user_view = UserView()
    user_view.menu()
