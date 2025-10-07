from db_connection import connection_bd
from degree import Degree

array_degree =[]
def insert_degree(degree, user, password):
    connection = connection_bd(user, password)
    if connection.is_connected():
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO carreras (Nombre) VALUES (%s)"
                val = (degree.get_name(),)
                cursor.execute(sql, val)
                connection.commit()
                return True
        except Exception as e:
            return None
        finally:
            connection.close()

def show_table(table, user, password):
    sql = f"SELECT * FROM {table}"
    connection = connection_bd(user, password)
    if connection.is_connected():
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                results = cursor.fetchall()
                for i in results:
                    degree = Degree(i[1],i[0])
                    array_degree.append(degree)
                return array_degree
        except Exception as e:
            return e
        finally:
            connection.close()



def update_degree(degree, user, password):
    connection = connection_bd(user, password)
    if connection.is_connected():
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE carreras SET Nombre = %s WHERE idCarrera = %s"
                val = (degree.get_name(), degree.get_id())
                cursor.execute(sql, val)
                connection.commit()
                return True
        except Exception as e:
            return None
        finally:
            connection.close()

def delete_degree(degree, user, password):
    connection = connection_bd(user, password)
    if connection.is_connected():
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM carreras WHERE Nombre = %s"
                val = (degree.get_name(),)
                cursor.execute(sql, val)
                connection.commit()
                cursor.close()
                connection.close()
                return True
        except Exception as e:
            return None
        finally:
            connection.close()