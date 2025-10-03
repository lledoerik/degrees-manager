from Carrera import Carrera
from db_utils import actualizar_tabla_carreras, eliminar_carrera, insertar_carrera, mostrar_tabla
from db_connection import coneccion_bd

seleccion_menu_p = None
seleccion_menu_carreras = None
usuario = None
contrasena = None
usuario_establecido = False

        
def menu_principal():
    print("1.Gestion carreras")
    print("0.Salir")

while not usuario_establecido:
    print("dime tu usuario de la bd")
    usuario = input()
    print("dime tu contraseña de la bd")
    contrasena = input()
    conneccion = coneccion_bd(usuario,contrasena)
    if conneccion is not None or False:
        print("Conexion establecida")
        conneccion.close()
        usuario_establecido = True
    else:
        print("Datos introduciodos incorrectos")

while seleccion_menu_p != 0:
    menu_principal()
    seleccion_menu_p = int(input())
    if seleccion_menu_p == 1:
        while seleccion_menu_carreras != 0:
            Carrera.menu_carreras()
            seleccion_menu_carreras = int(input())
            if seleccion_menu_carreras == 1:
                print(mostrar_tabla("carreras", usuario, contrasena))
            elif seleccion_menu_carreras == 2:
                nombre = input("Dime el nombre de la carrera que quieres insertar: ")
                carrera = Carrera(nombre)
                if insertar_carrera(carrera, usuario, contrasena):
                    print("Carrera insertada correctamente en la bd")
            elif seleccion_menu_carreras == 3:
                print(mostrar_tabla("carreras", usuario, contrasena))
                print("Dime el id de la carrera que quieres cambiar: ")
                id = int(input())
                print("Dime el nombre que deberia tener: ")
                carrera = Carrera(input(), id)
                if actualizar_tabla_carreras(carrera, usuario, contrasena):
                    print("Se ha actulizado el nombre de la carrera")
                
            elif seleccion_menu_carreras == 4:
                print(mostrar_tabla("carreras", usuario, contrasena))
                print("dime el id de lacarrera que quieres eliminar: ")
                carrera = Carrera()