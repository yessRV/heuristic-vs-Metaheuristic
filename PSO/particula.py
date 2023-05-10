from msilib.schema import Class
from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id, origen:dict, destino:dict,velocidad,color:dict):
        self.__id = id
        self.__origen = origen
        self.__destino = destino
        self.__velocidad = velocidad
        self.__color = color
        self.__distancia = distancia_euclidiana(origen["x"], destino["x"], origen["y"], destino["y"])

    def __str__(self):
        return (
            "ID: " + str(self.__id) + "\n"
            "Origen: (" + str(self.__origen["x"]) + "," + str(self.__origen["y"]) + ")\n"
            "Destino: (" + str(self.__destino["x"]) + "," + str(self.__destino["y"]) + ")\n"
            "Velocidad: " + str(self.__velocidad) + "\n"
            "Color: (" + str(self.__color["red"]) + "," + str(self.__color["green"]) + "," + str(self.__color["blue"]) + ")\n"
            "Distancia: " + str(self.__distancia) + "\n"
        )

    def to_dict(self):
        return{
            "id": self.__id,
            "origen": self.__origen,
            "destino": self.__destino,
            "velocidad": self.__velocidad,
            "color": self.__color,
        }

    @property
    def id(self):
        return self.__id

    @property
    def origen(self):
        return self.__origen

    @property
    def destino(self):
        return self.__destino

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def color(self):
        return self.__color

    @property
    def distancia(self):
        return self.__distancia