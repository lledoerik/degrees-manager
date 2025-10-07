from degree import Degree
from dao_degree import dao_degree
import requests as req

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
    con = req.get("http://localhost:5000/login", params={"user": user, "password": password})
    if con is not None or False:
        print("Conexion establecida")
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
                response = req.get("http://localhost:5000/show",
                                   params={"table": "carreras", "user": user, "password": password})
                if response.status_code == 200:
                    data = response.json()  # lista de diccionarios
                    degrees = [Degree.from_dict(item) for item in data]  # reconstruyes tus objetos
                    for d in degrees:
                        print(f"{d.get_id()}: {d.get_name()}")
                else:
                    print("Error:", response.status_code)

            elif degree_menu == 2:
                name = input("Inserta el nombre de la carrera a crear: ")
                response = req.get("http://localhost:5000/insert",
                                   params={"degree": name, "user": user, "password": password})
                if response.status_code == 200:
                    data = response.json()
                    degree = Degree(name)
                    print("Carrera insertada correctamente en la base de datos")
                else:
                    print("Error:", response.status_code)

            elif degree_menu == 3:
                response = req.get("http://localhost:5000/update",
                                   params={"table": "carreras", "user": user, "password": password})
                print(show_degrees("carreras", user, password))
                id_degree = int(input("Introduce el ID de la carrera a modificar: "))
                new_name = input("Introduce el nuevo nombre de la carrera: ")
                if response.status_code == 200:
                    degree = Degree(new_name, id_degree)
                    print("Se ha actulizado el nombre de la carrera")
                else:
                    print("Error:", response.status_code)

            elif degree_menu == 4:
                response = req.get("http://localhost:5000/delete",
                                   params={"table": "carreras", "user": user, "password": password})
                print(show_degrees("carreras", user, password))
                degree_name = input("Indica la carrera a eliminar: ")
                if response.status_code == 200:
                    degree = Degree(input().lower())
                    print("Se ha eliminado la carrera")
                else:
                    print("Error: ", response.status_code)
