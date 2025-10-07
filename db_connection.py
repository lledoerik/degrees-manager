import mysql.connector

host = "localhost"
database = "universidad"

class db_connection:
    def __init__(self,user,password):
        self.__user = user
        self.__password = password
  
    def connection_bd(self):
        try:
            connection = mysql.connector.connect(
                host=host,
                user=self.get_user(),
                password=self.get_password(),
                database=database
            )
            if connection.is_connected():
                return connection
        except mysql.connector.Error as err:
            return None
    
    def get_user(self):
        return self.__user
    
    def get_password(self):
        return self.__password
    
    def set_user(self,user):
        self.__user = user
        
    def set_password(self,password):
        self.__password = password
            