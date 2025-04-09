# Creazione della classe
class Automobile:
    numero_di_ruote = 4
    def __init__(self, marca, modello): # __init__ è il costruttore 
        self.marca = marca
        self.modello = modello
    def stampa_info(self):
        print("L'automobile è una", self.marca, self.modello)

# Creazione dell'oggetto
auto = Automobile("Fiat", "Panda")

auto.stampa_info()
