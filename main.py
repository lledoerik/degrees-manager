from degree import Degree
from dao_degree import update_table, delete_table, create_table, show_table
from db_connection import connection_bd

select_menu_p = None
user = None
password = None
user_connection = False


def main_menu():
    print("1.Gestion carreras")
    print("0.Salir")


while not user_connection:
    print("dime tu usuario de la bd")
    user = input()
    print("dime tu contraseña de la bd")
    password = input()
    connection = connection_bd(user, password)
    if connection is not None or False:
        print("Conexion establecida")
        connection.close()
        user_connection = True
    else:
        print("Datos introduciodos incorrectos")

while select_menu_p != 0:
    main_menu()
    select_menu_p = int(input())
    if select_menu_p == 1:
        degree_menu = None
        while degree_menu != 0:
            Degree.degrees_manager_menu()
            degree_menu = int(input())
            if degree_menu == 1:
                print(show_table("carreras", user, password))
            elif degree_menu == 2:
                name = input("Inserta el nombre de la carrera a crear: ")
                degree = Degree(name)
                if create_table(degree, user, password):
                    print("Carrera insertada correctamente en la base de datos")
            elif degree_menu == 3:
                print(show_table("carreras", user, password))
                print("Inserta el id de la carrera que a modificar: ")
                id_degree = int(input())
                print("Indica el nuevo nombre de la carrera: ")
                degree = Degree(input(), id_degree)
                if update_table(degree, user, password):
                    print("Se ha actulizado el nombre de la carrera")

            elif degree_menu == 4:
                print(show_table("carreras", user, password))
                print("Indica la carrera a eliminar: ")
                degree = Degree(input().lower())
                if delete_table(degree, user, password):
                    print("Se ha eliminado la carrera")
