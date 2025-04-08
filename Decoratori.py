def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione() # questa funzione viene utilizzata come parametro
        print("Dopo l'esecuzione della funzione")
    return wrapper

@decoratore
def saluta():
    print("Ciao!")

saluta()    