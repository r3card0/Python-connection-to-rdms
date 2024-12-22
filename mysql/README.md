# Connection to Mysql

This project implements two scripts to perform connection to a mysql rdms and create a dataframe with pandas.

## Installation
```bash
pip install pandas mysqlclient mysql-connector-python
```

## config file
The [config.py](/mysql/config.py) file requires to import the class **ConfigParser** from the module **configparser** [See configparser documentation](https://wiki.python.org/moin/ConfigParserExamples)

This module lets to parse the database authentication credencials taken from an 'INI' file that most been created previously. [See example file]()

Aquí tienes una tabla que resume los métodos de la biblioteca `configparser`, su propósito general, y los métodos específicos utilizados en el código proporcionado.

| **Elemento**         | **Propósito**                                                                 | **Métodos/Submétodos**                                    | **Propósito del método/submétodo**                                          |
|-----------------------|-------------------------------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------------------------|
| `configparser`        | Librería estándar para manejar archivos de configuración en formato INI.      | N/A                                                      | Permite leer, escribir y manipular configuraciones almacenadas en archivos. |
| `ConfigParser`        | Clase principal para manejar archivos INI.                                   | `read(filename)`                                         | Lee el archivo de configuración especificado por la ruta `filename`.       |
|                       |                                                                               | `has_section(section)`                                   | Verifica si existe una sección específica en el archivo de configuración.  |
|                       |                                                                               | `items(section)`                                         | Devuelve todos los pares clave-valor de una sección específica.            |

### Descripción de cada método:

1. **`read(filename)`**: 
   - Lee el archivo de configuración ubicado en la ruta `filename`.
   - En el código, esto se utiliza para cargar el archivo INI que contiene las configuraciones de la base de datos.

2. **`has_section(section)`**: 
   - Verifica si el archivo de configuración tiene una sección específica.
   - En este caso, se utiliza para confirmar que la sección `postgres` existe en el archivo.

3. **`items(section)`**: 
   - Recupera los pares clave-valor de una sección específica en forma de una lista de tuplas.
   - En el código, estas parejas se almacenan como un diccionario `db` para su uso posterior.

### Propósito General del Código:
Este fragmento de código carga las configuraciones de una base de datos desde un archivo INI, verifica que la sección de configuración existe, y devuelve los parámetros como un diccionario.



## connect_mysql file
The [connect_mysql](/mysql/connect_mysql.py) file, requires to import *mysql.connector* library and also needs to import the class **Config** from the module **config** located on [config](/mysql/config.py) file.

In the **Connect** class it's defined the instance method *connect*, where are getting the parameters to perform the connection to the Mysql database.

To run succesfully the instance method into the dataframe script.


## test file
The [test](/mysql/test.py) file requires to import the library pandas and import the class **Connect** from the module *mysql_connect*
