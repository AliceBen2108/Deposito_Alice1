# Esercizio 1

# Chiedo all'utente di inserire un numero
numero = int(input("Inserisci un numero: "))

# Imposto la variabile di controllo
continua = True

# Avvio il ciclo che continua finché la variabile continua è True
while continua:
    # Uso range() per fare il conto alla rovescia
    for i in range(numero, -1, -1):  # Parte dal numero, va fino a 0 incluso, decrementando di 1
        print(i)
    
    # Chiedo all'utente se vuole ripetere
    ripetere = input("Vuoi ripetere?: ").lower()
    
    # Se l'utente risponde "no", imposto continua su False per fermare il ciclo
    if ripetere != "si":
        print("Fine")
        continua = False
    else:
        # Chiedo un nuovo numero per il conto alla rovescia
        numero = int(input("Inserisci un altro numero: "))


# Esercizio 2

# Lista per salvare i numeri pari trovati
numeri_pari = []

# Ciclo finché non abbiamo trovato 5 numeri pari
while len(numeri_pari) < 5:
    numero = int(input("Inserisci un numero: "))
    
    if numero % 2 == 0:
        print("Il numero è pari")
        numeri_pari.append(numero)
    else:
        print("Il numero non è pari")

# Alla fine stampa i numeri pari raccolti
print("Hai inserito 5 numeri pari:", numeri_pari)