import matplotlib.pyplot as plt 

x1 = [1,3,5,7,9]
y1 = [2,3,7,1,0]

titulo = "Scatterplot: grafico de dispersao"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x,y, color="k", linestyle=":")
plt.scatter(x,y,label="Meus pontos", color="r", marker=".", s=200)
plt.legend()
plt.show
