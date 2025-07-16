
import matplotlib.pyplot as plt


categorias = ['Iphone', 'Motorola', 'Samsung', 'Sony', 'LG', 'Xiaomi', 'Asus', 'Huawei', 'OnePlus', "Oppo"], 
quantidade = [40,35,50,43,50,55,48,49,51,60]

plt.bar(categorias, quantidade)
plt.title("Marca de celulares mais famosas")
plt.xlabel("Marcas")
plt.ylabel("Ranking")

plt.show()