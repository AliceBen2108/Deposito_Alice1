import pandas as pd
import numpy as np

data = {
    "nome": ['Alice', 'Bob', 'Carla', 'None', 'Carla', 'Alice', 'Bob'],
    "età": np.linspace(0, 80, 7, dtype=int),
    "città": ['Roma', 'None', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Roma'],
    "salario": np.linspace(1000, 50000, 7, dtype=int)
}

df = pd.DataFrame(data)

print(df)

# Aggiungo dei valori nulli nelle colonne età e salario
df.loc[1, 'età'] = np.nan  
df.loc[3, 'salario'] = np.nan  

# 2: Prime e ultime 5 righe
print(df.head(5)) 
print(df.tail(5))  

# 3
print(df.dtypes)

# 4: Statistiche descrittive
print(df[["età", "salario"]].mean()) 
print(df[["età", "salario"]].std())  
print(df[["età", "salario"]].median()) 

# 5: Rimuovo i duplicati
df1 = df.drop_duplicates()

# 6: Identifico i valori mancanti e li sostituisco con la mediana
print(df1.isnull())
df1['età'].fillna(df1['età'].median(), inplace=True)
df1['salario'].fillna(df1['salario'].median(), inplace=True)

# 7: Classifico le persone in base all'età
def classifica_eta(eta):
    if eta < 30:
        return "giovane"
    elif eta < 60:
        return "adulto"
    else:
        return "senior"

df1["categoria età"] = df1["età"].apply(classifica_eta)
print(df1)

# 8: salvo il file in un csv
df1.to_csv('dataset.csv')  


