import sqlite3

# Nos conectamos a la base de datos (si no existe la crea)
conexion = sqlite3.connect("base_prueba.db")
# Creamos (si no existe) una tabla creada alumnos con sus campos
conexion.execute("""create table if not exists alumnos(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar,
                    edad integer
                    )""")
conexion.close()
conexion = sqlite3.connect("base_prueba.db")
# Insertamos dos alumnos
conexion.execute("Insert into alumnos(NOMBRE, EDAD) values(?,?)", ("FRANCISCO", 19))
conexion.execute("Insert into alumnos(NOMBRE, EDAD) values(?,?)", ("JESUS", 19))
# Este es necesario para que se ejecuten lñas consultas anteriores
conexion.commit()

# Recuperamos un elementos de la tabla alumnos y lo imprimimos
alumno = conexion.execute("select * from alumnos where nombre = 'JESUS'")
# Esto es para solamente traer el primero o bien para traer uno
fila = alumno.fetchone()
#imprimimos la fila (el alumno)
print(fila)
# Cerramos la conexión con SQLITE
conexion.close()