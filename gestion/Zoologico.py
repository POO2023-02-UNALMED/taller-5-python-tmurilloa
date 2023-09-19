
class Zoologico:
    _zonas = []
    def __init__(self,nombre,ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion

    def agregarZonas(cls,zona):
        cls._zonas.append(zona) 

    def cantidadTotalAnimales(cls):
        totalAnimales = 0
        for i in cls._zonas:
            totalAnimales += cls._zonas.cantidadAnimales()
        return totalAnimales
    
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre = nombre
    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    def getZonas(cls):
        return cls._zonas
    
        