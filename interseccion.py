import sympy as spy
from matplotlib import pyplot as plt

titulo = input("Introduzca el titulo: ")
titulo_fig = input("Introduzca el titulo del archivo: ")
a = float(input("Ingrese la pendiente de la demanda (positivo): "))
b = float(input("Ingrese el termino independiente de la demanda: "))
c = float(input("Ingrese la pendiente de la oferta: "))
d = float(input("Ingrese el termino independiente de la oferta: "))
x = spy.Symbol("x")
corte_x = round(b/a)
f_d = -a*x+b
f_o = c*x+d
point_x = []
point_y_d = []
point_y_o = []
point_neutral_x = (-b+d)/(-a-c)
point_neutral_y = f_o.subs(x, point_neutral_x)
for i in range(corte_x+1):
    point_x.append(i)
    point_y_d.append(f_d.subs(x, i))
    point_y_o.append(f_o.subs(x, i))
plt.scatter(point_neutral_x, point_neutral_y, color="black")
plt.plot(point_x, point_y_o)
plt.plot(point_x, point_y_d)
plt.title(titulo)
plt.ylabel("Precio")
plt.xlabel("Unidades")
plt.savefig("graficos/"+titulo_fig+".png", bbox_inches="tight")
plt.show()
