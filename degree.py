class Degree:
    def __init__(self, name, id=None):
        self.set_name(name)
        self.set_id(id)

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id
    
    def to_dict(self):
        return {
            "name": self.__name,
            "id": self.__id
        }
        
    @classmethod
    def degrees_manager_menu(self):
        print("1.Mostrar carreras")
        print("2.Insertar carrera")
        print("3.Actualizar carrera")
        print("4.Eliminar carrera")
        print("0.Volver al menu principal")
   

    @classmethod
    def from_dict(cls, data):
        return cls(name=data["name"], id=data["id"])