from database import Database

class PasswordManager:
    def __init__(self):
        self.db = Database()

    def store_password(self, account, username, password):
        self.db.insert_password(account, username, password)
        print("Password stored successfully.")

    def retrieve_password(self, account):
        return self.db.fetch_password(account)

    def list_accounts(self):
        return self.db.fetch_all_accounts()

    def __del__(self):
        self.db.close()
