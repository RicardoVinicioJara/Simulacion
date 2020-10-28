import random
import matplotlib.pyplot as plt

valores_salidas = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}


def generar_valores(cantidad):
    for n in range(0,cantidad):
        numero = random.randint(1, 12)
        valores_salidas[str(numero)] += 1

def graficar():
    plt.bar(range(len(valores_salidas)), list(valores_salidas.values()), align='center')
    plt.xticks(range(len(valores_salidas)), list(valores_salidas.keys()))
    plt.show()

if __name__ == '__main__':
    generar_valores(1000)
    graficar()