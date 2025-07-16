
import matplotlib.pyplot as plt


categorias = ['Python', 'Java', 'C', 'SQL', 'HTML']
quantidade = [80,65,40,50,69]

plt.bar(categorias, quantidade)
plt.title("Linguagem mais famosas")
plt.xlabel("Linguagens")
plt.ylabel("Quantidade")

plt.show()