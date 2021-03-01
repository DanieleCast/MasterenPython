from sqlite3.dbapi2 import DatabaseError
import mysql.connector

#Conexión
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "master_python"
)
#Conexión correcta


print(database)

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

#cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) AUTO_INCREMENT NOT NULL,
    marca VARCHAR(40) NOT NULL,
    modelo VARCHAR(40) NOT NULL,
    precio float(10,2) NOT NULL,
    CONSTRAINT pk_vehiculo PRIMARY KEY (id)
)
""")

cursor.execute("SHOW TABLES")

for tables in cursor:
    print(tables)