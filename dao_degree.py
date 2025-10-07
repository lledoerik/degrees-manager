from db_connection import db_connection
from degree import Degree

array_degree =[]
class dao_degree:
    def __init__(self):
        self.carrera = Degree(name="")
        self.__conn = None
        
    def login(self, con):
        conn = con.connection_bd()
        if conn and conn.is_connected():
            self.set_conn(conn)
            return True
        return False

        
    def get_conn(self):
        return self.__conn
    
    def set_conn(self,conn):
        self.__conn = conn
               
    def insert_degree(self,degree):
        conn = self.get_conn()
        if conn.is_connected():
            try:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO carreras (Nombre) VALUES (%s)"
                    val = (degree.get_name(),)
                    cursor.execute(sql, val)
                    conn.commit()
                    return True
            except Exception as e:
                return None
            
    def show_degrees(self, table):
        array_degree = []
        conn = self.get_conn()
        if conn and conn.is_connected():
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"SELECT * FROM {table}")
                    results = cursor.fetchall()
                    for i in results:
                        degree = Degree(i[1], i[0])
                        array_degree.append(degree)
                return array_degree
            except Exception as e:
                raise e

    def update_degree(self,degree):
        if self.get_conn().is_connected():
            try:
                with self.get_conn().cursor() as cursor:
                    sql = "UPDATE carreras SET Nombre = %s WHERE idCarrera = %s"
                    val = (degree.get_name(), degree.get_id())
                    cursor.execute(sql, val)
                    self.get_conn().commit()
                    return True
            except Exception as e:
                return None
            finally:
                self.get_conn().close()

    def delete_degree(self, degree):
        if self.get_conn().is_connected():
            try:
                with self.get_conn().cursor() as cursor:
                    sql = "DELETE FROM carreras WHERE Nombre = %s"
                    val = (degree.get_name(),)
                    cursor.execute(sql, val)
                    self.get_conn().commit()
                    cursor.close()
                    return True
            except Exception as e:
                return None
            finally:
                self.get_conn().close()
                
        