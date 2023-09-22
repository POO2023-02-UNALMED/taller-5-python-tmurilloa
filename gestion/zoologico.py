
class Zoologico:
    _zonas = []
    def __init__(self,nombre,ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion

    @classmethod
    def agregarZonas(cls,zona):
        cls._zonas.append(zona) 
    
    @classmethod
    def cantidadTotalAnimales(cls):
        totalAnimales = 0
        for i in range(len(cls._zonas)):
            x = cls._zonas[i].cantidadAnimales()
            totalAnimales += x
        return totalAnimales
    
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre = nombre
    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    @classmethod
    def getZona(cls):
        return cls._zonas

