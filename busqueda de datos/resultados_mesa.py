from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model

df = pd.read_csv("csv\VOTOS_X_ESTADO.csv", sep=",")
reg = linear_model.LinearRegression()
reg.fit(df[["EG"]], df.VOTOS_TOTALES)
print(reg.predict([[1]]))
