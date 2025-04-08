# Tipo numerico
intero = 10
numero_con_la_virgola = 5.5 # la virgola nei linguaggi di programmazione si fa con il punto

intero = int(input("inserisci un numero intero")) 
virgola = float(input("inserisci un numero con la virgola")) 

# Tipo semantico
stringa = input("inserisci una parola")
# Metodi
s = "ciao, mondo!"
print(len(s))
print(s.lower())
print(s.upper())
print(s.split())
print(s.replace("mondo" , "universo"))

carattere = chr(input("inserisci una singola lettera"))

# Tipi booleani
x = False
y = True

print(5>11)
print(13<50)
print(5>10 and 5>12)
print(5<10 or 5>12)
print(not 5>12)

# Liste
lista_dati = [1,2,3,4]
lista_dati1 = [1, "mirko", True]
lista_dati2 = []

print(lista_dati)
print(lista_dati1[2])
lista_dati1[1] = 10
lista_dati.sort()
print(lista_dati)

numeri = [1,3,2,5,4]
print(len(numeri))
numeri.append(6)
print(numeri)
numeri.remove(6)
print(numeri)
numeri.sort()
print(numeri)
numeri.insert (2, 10)

# per popolare una lista vuota utilizzo append
inserimento = int(input("inserisci un numero"))
lista_dati2.append(inserimento)
inserimento =int(input("inserisci un numero"))
lista_dati2.append(inserimento)
print(lista_dati2)






