import mysql.connector

host = "localhost"
database = "Universidad"
def coneccion_bd(user, password):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            return connection
    except mysql.connector.Error as err:
        return None