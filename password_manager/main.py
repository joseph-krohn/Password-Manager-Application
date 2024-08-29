from manager import PasswordManager

def main():
    manager = PasswordManager()
    
    while True:
        print("\nPassword Manager")
        print("1. Store a new password")
        print("2. Retrieve a password")
        print("3. List all accounts")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            account = input("Enter account name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            manager.store_password(account, username, password)
        elif choice == "2":
            account = input("Enter account name: ")
            password_info = manager.retrieve_password(account)
            if password_info:
                print(f"Username: {password_info[0]}, Password: {password_info[1]}")
            else:
                print("Account not found.")
        elif choice == "3":
            accounts = manager.list_accounts()
            if accounts:
                for account in accounts:
                    print(f"- {account}")
            else:
                print("No accounts stored.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
