from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model

df = pd.read_csv("csv\homeprices.csv", sep=";")
reg = linear_model.LinearRegression()
reg.fit(df[["area"]], df.price)
d = pd.read_csv("csv/areas.csv", sep=";")
p = np.round(reg.predict(d)/10, 2)
print(p)
d["prices"] = p
d.to_csv("csv/predict.csv")
new_d = pd.read_csv("csv/predict.csv")
plt.plot(new_d.area, new_d.prices)
plt.show()
