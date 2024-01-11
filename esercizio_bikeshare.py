import pandas as pd

# Imposta l'opzione di visualizzazione per mostrare tutte le colonne
pd.set_option('display.max_columns', None)

file1_path = 'C:\\Users\\Lenovo\\OneDrive\\Desktop\\esercitazione\\202004-divvy-tripdata.csv'

df1 = pd.read_csv(file1_path)
print(df1)
