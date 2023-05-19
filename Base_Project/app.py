from app import app

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            while True:
                print_user_menu()
                user_choice = input("Enter your choice: ")
                if user_choice == '5':
                    break
                handle_user_menu_choice(user_choice)
        elif choice == '2':
            while True:
                print_role_menu()
                role_choice = input("Enter your choice: ")
                if role_choice == '5':
                    break
                handle_role_menu_choice(role_choice)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()