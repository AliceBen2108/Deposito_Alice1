import numpy as np

# Creazione di un array
arr = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)
print(arr2d)

# Utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape)
print("Dimensioni dell'array:", arr.ndim) # numero delle righe
print("Tipo di dati:", arr.dtype)
print("Numero di elementi:", arr.size)
print("Somma di elementi:", arr.sum())
print("Media degli elementi:", arr.mean())
print("Valore massimo:", arr.max())
print("Indice del valore massimo:", arr.argmax())

# Funzione arange
arr = np.arange(10)
print(arr)

# Funzione reshape
arr = np.arange(6)
reshaped_arr = arr.reshape((2,3))
print(reshaped_arr)

# Indexing e Slicing: Esempio 1
arr = np.array([1, 2, 3, 4, 5])

# Indexing
print(arr[0])

# Slicing
print(arr[1:3])

# Boolean Indexing
print(arr[arr> 2])

# Indexing e Slicing: Esempio 2
arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

# Slicing sulle righe
print("Es 1: ", arr_2d[1:3])

# Slicing sulle colonne
print("Es 2: ", arr_2d[:, 1:3])

# Slicing misto
print("Es 3: ", arr_2d[1:, 1:3])

# Slicing: Esempio 3
arr = np.array([0,1,2,3,4,5,6,7,8,9])

# Slicing di base
print(arr[2:7])

# Slicing con passo
print(arr[1:8:2])

# Omettere start e stop
print(arr[:5])
print(arr[5:])

# Utilizzare indici negativi
print(arr[-5:])
print(arr[:-5])

# Fancy indexing
arr = np.array([10, 20, 30, 40, 50])

indices = np.array([1, 3])
print(arr[indices])

indices = [0, 2, 4]
print(arr[indices])