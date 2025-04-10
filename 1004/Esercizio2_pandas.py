import pandas as pd
import numpy as np

# Creazione dei dati
data = {
    "prodotto": ['Mela', 'Banana', 'Mela', 'Pera', 'Banana', 'Arancia', 'Pera', 'Mela', 'Mela', np.nan],
    "quantità": [10, 15, 10, 20, np.nan, 5, 20, 15, 10, 8],
    "prezzo unitario": [1.2, 0.5, 1.2, 1.5, 0.5, 0.8, np.nan, 1.2, 1.2, 1.0],
    "città": ['Roma', 'Milano', 'Roma', 'Napoli', 'Napoli', 'Roma', 'Milano', 'Roma', 'Napoli', np.nan]
}

# Creazione del DataFrame
df = pd.DataFrame(data)

# Stampa del DataFrame
print(df)

# 2: Prime e ultime 5 righe
print(df.head(5)) 
print(df.tail(5)) 

# Pulizzia dataframe
df = df.drop_duplicates()
df = df.dropna()

# 3: Aggiungiamo una nuova colonna: la persona maggiorenne
df["totale_vendite"] = df["quantità"] * df["prezzo unitario"]
print(df)

# 4: groupby
df_raggruppato = df.groupby('prodotto')['totale_vendite'].sum()
print(df_raggruppato)

# 5: 
df_quantità = df.groupby('prodotto')['quantità'].max()
print(df_quantità)

# 6: 
df_maxcittà = df.groupby('città')['totale_vendite'].max()
print(df_maxcittà)

# 7 
df_2 = df[df["totale_vendite"] > 1000]
print(df_2)
