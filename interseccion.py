from sympy import *
from matplotlib import pyplot as plt

titulo = input("Introduzca el titulo: ")
x = Symbol("x")
y=Symbol("y")
titulo_fig = input("Introduzca el titulo del archivo: ")
f_d = sympify(input("Ingrese una funcion de demanda x: "))
f_d_eq = Eq(f_d, y)
f_d_zero = Eq(f_d, 0)
f_o = sympify(input("Ingrese una funcion de oferta x: "))
f_o_eq = Eq(f_o, y)
corte_x = round(nsolve(f_d_zero, 1))
print(corte_x)
solution = nsolve([f_o_eq, f_d_eq], [x, y],[5,5],dict=True)
point_x = []
point_y_d = []
point_y_o = []
point_neutral_x = solution[0][x]
point_neutral_y = solution[0][y]
for i in range(corte_x+5):
    point_x.append(i)
    point_y_d.append(f_d.subs(x, i))
    point_y_o.append(f_o.subs(x, i))
plt.scatter(point_neutral_x, point_neutral_y, color="black")
plt.plot(point_x, point_y_o,color="green")
plt.plot(point_x, point_y_d,color="red")
plt.title(titulo)
plt.ylabel("Precio")
plt.xlabel("Unidades")
plt.legend(["Punto de Equilibrio","Oferta","Demanda"])
plt.savefig("graficos/"+titulo_fig+".png", bbox_inches="tight")
plt.show()
