# Connection to Mysql

This project implements two scripts to perform connection to a mysql rdms and create a dataframe with pandas.

## Installation
```bash
pip install pandas mysqlclient mysql-connector-python
```

## config file
The [config.py](/mysql/config.py) file requires to import the class **ConfigParser** from the module **configparser** [See configparser documentation](https://wiki.python.org/moin/ConfigParserExamples)

This module lets to parse the database authentication credencials taken from an 'INI' file that most been created previously. [See example file]()



## connect_mysql file
The [connect_mysql](/mysql/connect_mysql.py) file, requires to import *mysql.connector* library and also needs to import the class **Config** from the module **config** located on [config](/mysql/config.py) file.

In the **Connect** class it's defined the instance method *connect*, where are getting the parameters to perform the connection to the Mysql database.

To run succesfully the instance method into the dataframe script.


## test file
The [test](/mysql/test.py) file requires to import the library pandas and import the class **Connect** from the module *mysql_connect*