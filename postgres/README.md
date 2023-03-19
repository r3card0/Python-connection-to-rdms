# Connection to Postgres

## Installation
```
pip install pandas psycopg2
```


## config file
Watch this [config explanation](/mysql/README.md#config-file)

[config.py](/postgres/config.py)

```
from configparser import ConfigParser

class Config:
    def __init__(self) -> None:
        self.parser = ConfigParser()

    def config(self,filename='/path/database.ini',section = 'postgres'):
        db = {}
        self.parser.read(filename)

        if self.parser.has_section(section):
            self.params = self.parser.items(section)
            for param in self.params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section,filename))
        
        return db
```


## Connect_postgres file
The connect_postgres file, requires to [install](/postgres/README.md#installation) and import [psycopg2](https://pypi.org/project/psycopg2/) library and also needs to import the class Config from the module config located on [config.py](/postgres/config.py) file.

In the Connect class it's defined the instance method connect, where are getting the parameters to perform the connection to the Postgres database.

```
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
```



To run succesfully the instance method into the dataframe script.

## Test file
This file is an example of how to perform the connection to a postgres database. It can be use the next code:
```
# global variables to connect
conn = Connect()
connection = conn.connect()
```
or
```
connection = Connect().connect()
```
```
from connect_postgres import Connect

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
```
