La biblioteca `psycopg2` es una herramienta popular para interactuar con bases de datos PostgreSQL desde Python. Aquí tienes una tabla que describe algunos de los métodos más comunes, su propósito, sintaxis correcta y ejemplos prácticos.

---

### **Métodos más comunes de `psycopg2`**

| **Método**                   | **Propósito**                                                                                       | **Sintaxis Correcta**                                                                         | **Ejemplo**                                                                                                                                                                 |
|------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `connect`                    | Establecer una conexión con la base de datos PostgreSQL.                                           | `conn = psycopg2.connect(dsn)`                                                               | ```python<br>import psycopg2<br>conn = psycopg2.connect(dbname='test', user='user', password='pass', host='localhost')```                                                |
| `cursor`                     | Crear un cursor para ejecutar comandos SQL.                                                       | `cur = conn.cursor()`                                                                         | ```python<br>cur = conn.cursor()```                                                                                                                                         |
| `execute`                    | Ejecutar una consulta SQL usando el cursor.                                                       | `cur.execute(sql, params)`                                                                   | ```python<br>cur.execute("INSERT INTO table_name (column) VALUES (%s)", ("value",))```                                                                                    |
| `fetchone`                   | Recuperar una fila del resultado de una consulta.                                                 | `row = cur.fetchone()`                                                                       | ```python<br>cur.execute("SELECT * FROM table_name")<br>row = cur.fetchone()```                                                                                           |
| `fetchall`                   | Recuperar todas las filas del resultado de una consulta.                                          | `rows = cur.fetchall()`                                                                      | ```python<br>cur.execute("SELECT * FROM table_name")<br>rows = cur.fetchall()```                                                                                           |
| `fetchmany`                  | Recuperar un número limitado de filas del resultado de una consulta.                              | `rows = cur.fetchmany(size)`                                                                 | ```python<br>cur.execute("SELECT * FROM table_name")<br>rows = cur.fetchmany(10)```                                                                                         |
| `commit`                     | Confirmar las transacciones realizadas en la conexión.                                            | `conn.commit()`                                                                              | ```python<br>conn.commit()```                                                                                                                                               |
| `rollback`                   | Deshacer transacciones en la conexión actual.                                                     | `conn.rollback()`                                                                            | ```python<br>conn.rollback()```                                                                                                                                             |
| `close`                      | Cerrar el cursor o la conexión para liberar recursos.                                             | `cur.close()` o `conn.close()`                                                              | ```python<br>cur.close()<br>conn.close()```                                                                                                                                 |
| `mogrify`                    | Devolver una cadena con una consulta SQL formateada correctamente.                                | `formatted_query = cur.mogrify(sql, params)`                                                | ```python<br>formatted_query = cur.mogrify("INSERT INTO table_name (column) VALUES (%s)", ("value",))```                                                                   |
| `set_session`                | Configurar las propiedades de la sesión actual.                                                   | `conn.set_session(autocommit=True, isolation_level='SERIALIZABLE')`                         | ```python<br>conn.set_session(autocommit=True)```                                                                                                                           |

---

### **Total de métodos en `psycopg2`**

El módulo `psycopg2` incluye varios métodos y atributos adicionales en sus clases principales, como `connection`, `cursor`, y utilidades. Según la documentación oficial hasta el momento, **la biblioteca tiene más de 50 métodos públicos** entre la conexión, el cursor y funciones utilitarias.

Algunos métodos avanzados adicionales son:
- `copy_from` y `copy_to`: Para copiar datos entre un archivo y una tabla de PostgreSQL.
- `nextset`: Navegar entre múltiples resultados de una consulta.
- Métodos relacionados con adaptadores de datos personalizados.

---

### Ejemplo Práctico Combinado
```python
import psycopg2

# Conectar a la base de datos
conn = psycopg2.connect(dbname='testdb', user='user', password='pass', host='localhost')
cur = conn.cursor()

try:
    # Crear una tabla
    cur.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        )
    """)

    # Insertar datos
    cur.execute("INSERT INTO categories (name) VALUES (%s)", ("Example",))
    
    # Confirmar transacción
    conn.commit()

    # Consultar datos
    cur.execute("SELECT * FROM categories")
    rows = cur.fetchall()
    for row in rows:
        print(row)
except Exception as e:
    print(f"Error: {e}")
    conn.rollback()
finally:
    # Cerrar cursor y conexión
    cur.close()
    conn.close()
```

---
