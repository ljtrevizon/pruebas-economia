import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv("csv/fee599e1-5668-4325-9619-49b5b4291aa1_Data.csv")
titulo=input("Introduzca el titulo: ")
titulo_fig=input("Introduzca el titulo del archivo: ")

plt.plot(df["Time"], df["United States [USA]"])
plt.plot(df["Time"], df["Japan [JPN]"])
plt.plot(df["Time"], df["Germany [DEU]"])
plt.plot(df["Time"], df["United Kingdom [GBR]"])
plt.plot(df["Time"], df["France [FRA]"])
plt.legend(["Estados Unidos", "Japon", "Alemania",
           "Reino Unido", "Francia"], loc="upper left")
plt.title(titulo)
plt.ylabel("porcentaje (%)")
plt.xlabel("Año")
plt.savefig("graficos/"+titulo_fig+".png",bbox_inches="tight")
plt.show()
