

import psycopg2 as p2
from config import Config

# global variables
x = Config()

class Connect:
    def __init__(self):
        self.params = x.config()

    def connect(self):
        self.connection = p2.connect(**self.params)
        return self.connection


if __name__ == "__main__":
    connection = Connect()
    connection.connect()
