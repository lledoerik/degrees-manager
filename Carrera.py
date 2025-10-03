from db_connection import coneccion_bd

class Carrera:
    def __init__(self, nombre, id=None):
        self.setNombre(nombre)
        self.setId(id)
    
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def setId(self,id):
        self.__id = id    
    
    def getNombre(self):
        return self.__nombre
    
    def getId(self):
        return self.__id
    
    @classmethod
    def menu_carreras(self):
        print("1.Mostrar carreras")
        print("2.Insertar carrera")
        print("3.Actualizar carrera")
        print("4.Eliminar carrera")
        print("0.Volver al menu principal")