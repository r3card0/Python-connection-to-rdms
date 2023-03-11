import mysql.connector as conn
from config import Config

# global variables
x = Config()

class Connect:
    def __init__(self):
        self.params = x.config()

    def connect(self):
        self.connection = conn.connect(**self.params)
        return self.connection


if __name__ == "__main__":
    mysql_connection = Connect()
    mysql_connection.connect()