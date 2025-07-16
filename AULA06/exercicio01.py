
import matplotlib.pyplot as plt


categorias = ['Laranja', 'Pera', 'Abacaxi', 'Uva', 'Banana', 'Morango', 'Kiwi', 'Tomate', 'Jaboticaba', 'Maça']
quantidade = [45,65,80,50,69,71,58,75,63,43]

plt.bar(categorias, quantidade)
plt.title("Frutas mais gostosas")
plt.xlabel("Nome das frutas")
plt.ylabel("Ranking")

plt.show()