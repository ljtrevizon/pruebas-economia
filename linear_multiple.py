from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model
import numpy as np
import random as rn

df = pd.read_csv("csv\economics_2.csv", sep=";")
data = pd.read_csv("csv\data.csv", sep=";")
for i in range(len(data.index)):
    data.loc[i, "pob_in_mm"] = round(
        (rn.randint(4500000, 7500000)/10000000), 3)
    data.loc[i, "ipc"] = round((rn.randint(1, 90)/100), 3)
    data.loc[i, "ppp_in_k"] = round((rn.randint(100, 25000)/10000), 3)
median = df.ipc.median()
df.fillna({"ipc": median}, inplace=True)
reg = linear_model.LinearRegression()
reg.fit(df[["year", "pob_in_mm", "ipc", "ppp_in_k"]], df.f_e)
fe = np.round(reg.predict(data[["year", "pob_in_mm", "ipc", "ppp_in_k"]]), 3)
for i in range(len(fe)):
    if fe[i] < 0:
        fe[i] = -(fe[i])
data["f_e"] = fe
data_merge = pd.concat([df, data], sort=False)
plt.plot(data_merge.year, data_merge.ppp_in_k, label="PPP")
plt.plot(data_merge.year, data_merge.pob_in_mm, label="Poblacion")
plt.plot(data_merge.year, data_merge.f_e, label="FE")
plt.plot(data_merge.year, data_merge.ipc, label="IPC")
plt.grid(True)
plt.legend()
plt.show()
