# esercizio 1
x = int(input("Scrivi un numero maggiore di 18"))

if x > 18:

    x = int(input("scrivi un numero minore di 50"))
    if x < 50:

        x = int(input("scrivi un numero maggiore di 50"))
        if x == 100:

            print("sei arrivato alla fine")
        
        else:
            print("hai scritto un numeor diverso da 100")
       
# esercizio 2   
lista =["mirko", "paolo", "pippo"]

scelta = input("scegli cosa vuoi fare")

if scelta.lower() == "elimina" :
    print(lista)
    scelta = input("scegli cosa vuoi eliminare")
    lista.remove(scelta)
    print(lista)
elif scelta.lower() == "aggiungi":
    scelta = input("scegli cosa vuoi aggiungere")
    lista.append(scelta)
    print(lista)
elif scelta.lower() == "modifica":
    print(lista)
    scelta = int(input("scegli quale posizione vuoi modificare da 0 a 2"))
    scelta2 = input("scegli cosa vuoi aggiungere")
    lista[scelta]= scelta2
    print(lista)
else:
    print("comando sbagliato")

# esercizio 3
# creazione di variabili
nome = ""
password = ""
id = 0
x = True

# condizioni
if x:
    nome = input("inserisci il tuo nickname")
    password = input("inserisci la tua pssword")
    id += 1

# login
if nome == "": # entretà qui se come input del nome ha messo ""
    print("non hai valorizzato")
else:
    nome_inserito = input("inserisci il tuo nickname")
    password_inserita = input("inserisci la tua password")
    if nome_inserito == nome and password_inserita == password:
        print("se loggato")
    else:
        print("credenziali errate")


