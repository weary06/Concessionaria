from abc import ABC
class Concessionaria(ABC):
    def __init__(self,targa,marca,modello,numeroDiPosti,prezzoDiBase):
        self.set_targa(targa)
        self.set_marca(marca)
        self.set_modello(modello)
        self.set_numeroDiPosti(numeroDiPosti)
        self.set_prezzoDiBase(prezzoDiBase)
    
    def setTarga(self,targa):
        self._targa=targa
    def setMarca(self,marca):
        self._marca=marca
    def setModello(self,modello):
        self._modello=modello
    def setNumeroDiPosti(self,numeroDiPosti):
        self._numeroDiPosti=numeroDiPosti
    def getTarga(self):
        return self._targa