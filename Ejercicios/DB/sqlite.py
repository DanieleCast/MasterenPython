import sqlite3

#Conexión
conexion = sqlite3.connect('pruebas.db')

#Crear Tabla
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
Titulo VARCHAR(255),
description text,
precio int(255)
);
""")

#GUARDAR CAMBIOS
conexion.commit()
#Insertar Datos
cursor.execute("INSERT INTO productos VALUES(null,'Primer Producto','Descripcion de producto1',1500)")
conexion.commit()




#insertar muchos productos de golpe
productos= [
    ("Computador","PC",500),
    ("lAPTOP","Lenovo",600),
    ("Celular","Samsung",700),
    ("Tablet","Apple",800),
    ("TV","Sony",900),
]

cursor.executemany("INSERT INTO productos VALUES(null,?,?,?)",productos)
conexion.commit()

#Actualizar
cursor.execute("UPDATE productos SET precio= 678 WHERE precio =1500")


#Listar Datos
cursor.execute("SELECT * FROM productos WHERE precio >= 500;")
print(cursor)

productos = cursor.fetchall()



for producto in productos:
    print("ID: ",producto[0])
    print("Titulo: ",producto[1])
    print("Descripcion: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

#Borrar Registros 
#cursor.execute("DELETE FROM PRODUCTOS")

#Sacar un elemento de la tabla
cursor.execute("SELECT precio FROM productos;")
producto = cursor.fetchone()
print(producto)




conexion.close()