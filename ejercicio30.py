import mysql.connector
config = {
    'user': 'root',      
    'password': '',    
    'host': 'localhost', 
    'database': 'ejercicio30' 
}

conexion = mysql.connector.connect(**config)
cursor = conexion.cursor()

def insertar():
    insertar = "INSERT INTO `informacion` (`Nombre`, `Sexo`, `Sangre`, `Contacto`) VALUES (%s, %s, %s, %s)"
    informacion = ("Pepe", "Masculino", "o+", 618)
    try:
        cursor.execute(insertar, (informacion))
        conexion.commit()
        print(f"Información insertada")
    except Exception as e:
        print(f"Error: {e}") 

def select():
    select = "SELECT * from `informacion` where `Nombre` = 'Edson'"
    try:    
        cursor.execute(select)
        datos = cursor.fetchall()
        print(f"{datos}")
    except Exception as e:
        print(f"Error: {e}")
    
def delete():
    delete = "DELETE from `informacion` WHERE `Nombre`= 'Borrar'"
    try:    
        cursor.execute(delete)
        conexion.commit()
        print(f"Registro borrado")

    except Exception as e:
        print(f"Error: {e}")
 

insertar()
select()
delete()

cursor.close()
conexion.close()