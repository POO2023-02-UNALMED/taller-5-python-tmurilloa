class Zona:
    _animales = []
    def __init__(self,nombre,zoo):
        self._nombre = nombre
        self._zoo = zoo

    def agregarAnimales(cls,animal):
        cls._animales.append(animal)
    def cantidadAnimales(cls):
        return len(cls._animales)
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre = nombre
    def getZoo(self):
        return self._zoo
    def setZoo(self, zoo):
        self._zoo = zoo
    def getAnimales(cls):
        return cls._animales