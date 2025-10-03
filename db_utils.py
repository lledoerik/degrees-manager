from db_connection import coneccion_bd
from Carrera import Carrera

def actualizar_tabla_carreras(carrera, usuario,contrasena):
        connection = coneccion_bd(usuario,contrasena)
        if connection.is_connected():
            try:
                with connection.cursor() as cursor:
                    sql = "UPDATE carreras SET Nombre = %s WHERE idCarrera = %s"
                    val = (carrera.getNombre(),carrera.getId())
                    cursor.execute(sql, val)
                    connection.commit()
                    return True                
            except Exception as e:
                return None
            finally:
                connection.close()

def eliminar_carrera(carrera,usuario,contrasena):
        connection = coneccion_bd(usuario,contrasena)
        if connection.is_connected():
            try:
                with connection.cursor() as cursor:
                    sql = "DELETE FROM carreras WHERE idCarrera = %s"
                    cursor.execute(sql, carrera.getIdd())
                    connection.commit()
                    return True
            except Exception as e:
                return None
            finally:
                connection.close()
                
            
def insertar_carrera(carrera,usuario,contrasena):
        connection = coneccion_bd(usuario,contrasena)
        if connection.is_connected():
            try:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO carreras (Nombre) VALUES (%s)"
                    val = (carrera.getNombre(),)
                    cursor.execute(sql, val)
                    connection.commit()    
                    return True
            except Exception as e:
                    return e
            finally:
                connection.close()
                
def mostrar_tabla(tabla, usuario, contrasena):
    sql = f"SELECT * FROM {tabla}"
    connection = coneccion_bd(usuario, contrasena)
    if connection.is_connected():
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                results = cursor.fetchall()
                return results
        except Exception as e:
            return e
        finally:
            connection.close()