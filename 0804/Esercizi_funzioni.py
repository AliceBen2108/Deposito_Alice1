# Esercizio 1

# Importo il modulo random
import random

# Definisco la funzione
def gioco():
    numero_casuale = random.randint(1, 100) # Sceglie un numero random intero

# Ciclo while
    while True:
        tentativo = input("Inserisci un numero: ")

        if tentativo.lower() == "esci":
            print("Sei uscito. Il numero corretto era:", numero_casuale)
            break

        tentativo = int(tentativo)

        if tentativo < numero_casuale:
            print("Il numero è troppo basso")
        elif tentativo > numero_casuale:
            print("Il numero è troppo alto")
        else:
            print("Hai indovinato il numero:", numero_casuale)
            break

# Richiamo la funzione
gioco()


# Esercizio 2

# Definisco la funzione
def fibonacci():
    n = int(input("Inserisci un numero: "))
    a, b = 0, 1

    while a <= n:
        print(a)
        a, b = b, a + b

# Eseguo la funzione
fibonacci()