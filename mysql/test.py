from connect_mysql import Connect
import pandas as pd

# global variables to connect
conn = Connect()
connection = conn.connect()

# sql query
def query():
    sql = """
    SELECT * FROM table1
    limit 5
    """
    return sql

# dataframe creation
def dataframe():
    df = pd.read_sql_query(query(),connection)
    df = df.copy(deep=True)
    return df

def run():
    print(dataframe())


if __name__ == "__main__":
    run()
