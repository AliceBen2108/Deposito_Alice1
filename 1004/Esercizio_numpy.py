# # Esercizio 1
# import numpy as np

# # 1: array di 12 numeri equidistanti tra 0 e 1
# arr = np.linspace(0, 1, 12)
# print("Es 1: ", arr)

# # 2: cambio la forma dell'array in una matrice 3x4
# matrice = arr.reshape(3, 4)
# print("Es 2: ", matrice)

# # 3: matrice 3x4 di numeri casuali tra 0 e 1
# matrice_casuale = np.random.rand(3, 4)
# print("Es 3: ", matrice_casuale)

# # 4: somma degli elementi di entrambe le matrici
# somma1 = matrice.sum()
# somma2 = matrice_casuale.sum()

# print("Es 4: ", somma1)
# print("Es 4: ", somma2)

# # Esercizio extra
# import numpy as np

# class Array:
#     def __init__(self):
#         self.array = None  # inizializzazione dell'attributo 

#     def crea_array_linspace(self, start, stop, num):
#         self.array = np.linspace(start, stop, num)
#         print(self.array)

# creatore = Array()
# creatore.crea_array_linspace(0, 1, 12)

# Esercizio 2
import numpy as np

class Array:
    def __init__(self):
        self.array_50 = None
        self.array_casuale = None
        self.array_somma = None

    def array(self, start = 0, stop = 10, num = 50):
        self.array_50 = np.linspace(start, stop, num)
        print("Es 1: ", self.array_50)

    def array1(self, num=50):
        self.array_casuale = np.random.rand(num)  # valori casuali tra 0 e 1
        print("Es 2: ", self.array_casuale)

    def somma_array(self):
        self.array_somma = self.array_50 + self.array_casuale # somma dei due array elemento per elemento
        print("Es 3: ", self.array_somma)

    def somma_totale(self):
        sum = self.array_somma.sum()
        print("Es 4: ", sum)

    def somma_maggiore_di_cinque(self):
        sum2 = self.array_somma[self.array_somma > 5].sum()
        print("Es 4: ", sum2)    

# Richiamo degli oggetti
array = Array() # definizione dell'oggetto
array.array()
array.array1()
array.somma_array()
array.somma_totale()
array.somma_maggiore_di_cinque()

