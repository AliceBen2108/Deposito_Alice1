# Esempio basilare
class Esempio():
    x = 10 

# Creazione oggetto basilare
oggetto_1 = Esempio()
oggetto_2 = Esempio()

# Modifica attributo
oggetto_1.x = 20
print(oggetto_1.x)

class Penna():
    altezza = 0
    larghezza = 0

    # Metodo speciale: Costruttore
    def __init__(self, h, l): # self rappresenta l'oggetto stesso
        self.altezza = h
        self.larghezza = l

oggetto_penna = Penna(10,7)

print(oggetto_penna.altezza)
print(oggetto_penna.larghezza)