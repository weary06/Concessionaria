class Concessionaria():
    veicoli = []
    def __init__(self,targa,marca,modello,numeroDiPosti,prezzoDiBase):
        Concessionaria.veicoli.append(self)
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
    def setPrezzoDiBase(self,prezzoDiBase):
        self._prezzoDiBase=prezzoDiBase

    def get_targa(self):
        return self._targa
    def get_Marca(self):
        return self._marca
    def get_modello(self):
        return self._modello
    def get_numeroDiPosti(self):
        return self._numeroDiPosti
    def get_prezzoDiBase(self):
        return self._prezzoDiBase

    def stampa_Veicoli(self,veicoli):
        print(veicoli)

class Autocarro(Concessionaria):
    def __init__(self,targa,marca,modello,numeroDiPosti,prezzoDiBase,capacitàDiCarico):
        super().__init__(targa,marca,modello,numeroDiPosti,prezzoDiBase)
        self.set_capacitàDiCarico(capacitàDiCarico)

    def set_capacitàDiCarico(self,capacitàDiCarico):
        self._capacitàDiCarico=capacitàDiCarico

#Prezzo autocarro = prezzo di base x capacità massima di carico

class Autoveicolo(Concessionaria):
    def __init__(self,targa,marca,modello,numeroDiPosti,prezzoDiBase,numeroDiPorte):
        super().__init__(targa,marca,modello,numeroDiPosti,prezzoDiBase)
        self.set_numeroDiPorte(numeroDiPorte)

    def set_NumeroDiPorte(self,numeroDiPorte):
        self._numeroDiPorte = numeroDiPorte
#Prezzo autoveicolo = prezzo di base x numero di porte

class Motoveicolo(Concessionaria):
    def __init__(self,targa,marca,modello,numeroDiPosti,prezzoDiBase,cilindrata):
        super().__init__(targa,marca,modello,numeroDiPosti,prezzoDiBase)
        self.set_cilindrata(cilindrata)

    def set_Cilindrata(self,cilindrata):
        self._cilindrata=cilindrata
    def get_Cilindrata(self):
        return self._cilindrata

#Prezzo motoveicolo = prezzo di base x cilindrata

