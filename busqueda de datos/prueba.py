import pandas as pd
import sqlite3
from pathlib import Path


Path('my_data.db').touch()
conn = sqlite3.connect('my_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE resultados (id int,COD_EDO int,EDO text, MUN text, PAR text, CENTRO text, MESA int, EG int, URL text)''')
base = pd.read_csv("csv/RESULTADOS_CENTRO_MESA_EG.csv")
base.to_sql('resultados', conn, if_exists='append', index=False)