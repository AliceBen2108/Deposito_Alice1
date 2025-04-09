# Creazione delle classi libro e biblioteca
class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def stampa_info(self):
        print(self.titolo)
        print(self.autore)

class Biblioteca:
    libri = []

    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)

    def stampa_libri(self):
        for libro in self.libri:
            libro.stampa_info()
 

# Menù per la gestione della biblioteca
biblioteca = Biblioteca()

while True:
    titolo = input("Inserisci il titolo (oppure 'fine' per uscire)")
    if titolo.lower() == "fine":
        break
    autore = input("Inserisci l'autore")
    nuovo_libro = Libro(titolo, autore)
    biblioteca.aggiungi_libro(nuovo_libro)

print("\nStampa dei libri nella biblioteca:")
biblioteca.stampa_libri()
