# if
numero = 10
if numero > 0:
    print("Il numero è positivo")

numero = -1
if numero > 0:
    print("Il numero è positivo")
else:
    print("Blocco Else")
# le condizioni di if e else non potranno mai essere stampate entrambe

numero = 100
if numero > 0:
    print("Il numero è positivo")
    if numero == 100:
        print("wow")
elif numero < -10:
    print("mega wow")
else:
    print("Blocco Else")

