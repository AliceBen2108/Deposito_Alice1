# Esercizio
import numpy as np

# 1: array di 20 numeri casuali tra 10 e 50
arr = np.random.randint(10, 51, size=20)
print(arr)

# 2: primi 10 elementi
print("2:", arr[:11])

# 3: ultimi cinque elementi
print("3:", arr[-5:])

# 4: elemenenti dal 5 al 15 incluso
print("4:", arr[5:16])

# 5: ogni terzo elemento
print("5:", arr[2:21:3])

# 6: trasformare gli elementi dal 5 al 10 escluso in 99
arr[5:10] = 99
print("6:", arr)

