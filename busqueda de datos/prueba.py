import pandas as pd
import sqlite3
from pathlib import Path

conn = sqlite3.connect('busqueda de datos\my_data.db')
c = conn.cursor()

c.execute('''update sqlite_sequence set seq=""''')
c.execute('''DELETE from resultados''')
original = pd.read_csv("csv\RESULTADOS_2024_CSV_V2.csv", encoding='latin-1')
original.to_sql('resultados', conn, if_exists='append', index=False)
print("Listo")