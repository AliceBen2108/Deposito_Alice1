# Esercizio 1
# Ciclo while
while True:
    numero = int(input("Inserisci un numero: "))
    
    if numero % 2 == 0:
        print("Pari")
    else:
        print("Dispari")

    ripetere = input("Vuoi ripetere?: ").lower()
    if ripetere == "no":
        print("Fine")
        break


# Esercizio 2
# Ciclo while
while True:
    numero = int(input("Inserisci un numero: "))

    if numero > 0:
        for i in range(numero, -1, -1):  # Parte dal numero, va fino a 0 incluso, decrementando di 1
            print(i)
        ripetere = input("Vuoi ripetere?: ").lower()
    if ripetere == "no":
        print("Fine")
        break

# Esercizio 3
# Lista di numeri da riempire
lista_numeri = []

# Ciclo while
while len(lista_numeri) < 4:
    numero = int(input("Inserisci un numero: "))
    lista_numeri.append(numero**2)

# Stampa la lista del quadrato dei numeri interi 
print(lista_numeri)


