# Connection to Postgres

## Installation
```
pip install pandas psycopg2
```


## config file
Watch this [config explanation](https://github.com/r3card0/Python-connection-to-rdms/tree/main/mysql#config-file)

## Connect_postgres file
The connect_postgres file, requires to import [psycopg2](https://pypi.org/project/psycopg2/) library and also needs to import the class Config from the module config located on config file.

In the Connect class it's defined the instance method connect, where are getting the parameters to perform the connection to the Postgres database.

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

