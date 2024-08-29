import sqlite3

class Database:
    def __init__(self, db_name="password_manager.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            account TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """)
        self.connection.commit()

    def insert_password(self, account, username, password):
        self.cursor.execute("""
        INSERT INTO passwords (account, username, password)
        VALUES (?, ?, ?)
        """, (account, username, password))
        self.connection.commit()

    def fetch_password(self, account):
        self.cursor.execute("SELECT username, password FROM passwords WHERE account = ?", (account,))
        return self.cursor.fetchone()

    def fetch_all_accounts(self):
        self.cursor.execute("SELECT account FROM passwords")
        return [row[0] for row in self.cursor.fetchall()]

    def close(self):
        self.connection.close()
