from particula import Particula
import json

class Lista:
    def __init__(self):
        self.__particulas = []
        self.__nodos = dict()

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0,particula)

    def mostrar(self):
        for v in self.__particulas:
            print(v)

    def lista_adyacencia(self):
        self.__nodos.clear()
        for particula in self.__particulas:
            key = (particula.origen["x"],particula.origen["y"])
            #key = "(" + str(particula.origen["x"]) + "," + str(particula.origen["y"]) + ")"
            if key not in self.__nodos:
                self.__nodos[key] = []
                self.__nodos[key].append([(particula.destino["x"],particula.destino["y"]),particula.distancia])
            else:
                repetido = False
                for arista in self.__nodos[key]:
                    if(arista == particula.destino):
                        repetido = True
                if not repetido:
                    self.__nodos[key].append([(particula.destino["x"],particula.destino["y"]),particula.distancia])
            ##DESTINO
            key = (particula.destino["x"],particula.destino["y"])
            if key not in self.__nodos:
                self.__nodos[key] = []
                self.__nodos[key].append([(particula.origen["x"],particula.origen["y"]),particula.distancia])
            else:
                repetido = False
                for arista in self.__nodos[key]:
                    if(arista == particula.origen):
                        repetido = True
                if not repetido:
                    self.__nodos[key].append([(particula.origen["x"],particula.origen["y"]),particula.distancia])
        return self.__nodos

    def __str__(self):
        return "".join(
            str(v) + "\n" for v in self.__particulas
        )

    def __len__(self):
        return(
            len(self.__particulas)
        )

    def __iter__(self):
        self.cont = 0

        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            avion = self.__particulas[self.cont]
            self.cont += 1
            return avion

        else:
            raise StopIteration

    def guardar(self,ubicacion):
        try:
            with open(ubicacion,'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista,archivo,indent = 5)
                return 1
        except:
            return 0

    def abrir(self,ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
                return 1
        except:
            return 0

    def ordenar_id(self):
        self.__particulas.sort(key=lambda particula:particula.id)

    def ordenar_distancia(self):
        self.__particulas.sort(key=lambda particula:particula.distancia)

    def ordenar_velocidad(self):
        self.__particulas.sort(key=lambda particula:particula.velocidad)