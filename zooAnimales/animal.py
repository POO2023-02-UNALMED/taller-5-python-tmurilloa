
class Animal:
    _totalAnimales = 0
    def __init__(self,nombre,edad,habitat,genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1
    
    def movimiento(self):
        return "desplazarse"
    def toString(self):
        resultado = f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        if self._zona != None:
            resultado += f", la zona en la que me ubico es {self._zona}, en el {self._zona.getZoo()}"
        return resultado
    @classmethod
    def totalPorTipo(cls):
        from .mamifero import cantidadMamiferos
        from .ave import cantidadAves
        from .anfibio import cantidadAnfibios
        from .reptil import cantidadReptiles
        from .pez import cantidadPeces   
        resultado = f"Mamiferos : {cantidadMamiferos()}\nAves : {cantidadAves()}\nReptiles : {cantidadReptiles()}\nPeces : {cantidadPeces()}\nAnfibios : {cantidadAnfibios()}"
        return resultado
    
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre = nombre
    def getEdad(self):
        return self._edad
    def setEdad(self,edad):
        self._edad = edad
    def getHabitat(self):
        return self._habitat
    def setHabitat(self,habitat):
        self._habitat = habitat
    def getGenero(self):
        return self._genero
    def setGenero(self,genero):
        self._genero = genero
    def getTotalAnimales(cls):
        return cls._totalAnimales
    def setTotalAnimales(cls,totalAnimales):
        cls._totalAnimales = totalAnimales