from .animal import Animal
class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
    
    @classmethod
    def cantidaAnfibios(cls):
        return len(cls._listado)
    def movimiento(self):
        return "saltar"
    @classmethod
    def crearRana(cls,nombre,edad,genero):
        rana = Anfibio(nombre,edad,"selva",genero,"rojo",True)
        cls.ranas += 1
        return rana
    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        salamandra = Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        cls.salamandras += 1
        return salamandra
    
    def setColorPiel(self,colorPiel):
        self._colorPiel = colorPiel
    def getColorPiel(self):
        return self._colorPiel
    def setVenenoso(self,venenoso):
        self._venenoso =  venenoso
    def isVenenoso(self):
        return self._venenoso
    def getListado(cls):
        return cls._listado
