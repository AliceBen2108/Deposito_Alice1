# Semantica dele funzioni
def nome_della_funzione ():
    pass

# Esempio di funzione
def saluta():
    print("ciao")

saluta()

# Funzione con parametri
def somma(x, y): # x e y sono play solder, ovvero i contenitori delle variabili reali che gli manderemo
    risultato = x + y
    print(risultato)

somma(1, 2)

# Esempio di funzione
def saluta_con_parametro(nome):
    print("ciao", nome)

saluta_con_parametro("Alice")


# Funzione di ritorno
def riporta_dato(x): 
    risultato = x * x
    return risultato

# Chiamata della funzione riporta_dato e stampa del risultato
numero = riporta_dato(3)
print(numero)  # oppure print(riporta_dato(3)) direttamente

somma = riporta_dato(3) + riporta_dato(3) + riporta_dato(3)
print(somma)

# Funzione con parametri standard
def funzione_standard(x = 1):
    return x + x

print(funzione_standard(4))
