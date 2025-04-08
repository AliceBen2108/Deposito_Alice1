# Lettura di file
file = open("esempiotesto.txt", "r") # "r" sta per modalità lettura

tutte_le_righe = file.read()
riga = file.readline()

print(tutte_le_righe)

file.close()

# Scrittura di file 
file = open("esempiotesto2.txt", "w") # "w" sta per modalità scrittura

file.write("sto modificando il file")
file.close()

# Modifica del file
file = open("esempiotesto.txt", "a")
file.write(" Sto aggiungendo al testo")
file.close()

# Apertura senza bisogno di chiusura
with open("esempio testo", "w") as file:
    file.write("auto chiudo la chiamata")

