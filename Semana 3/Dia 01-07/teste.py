import numpy as np

producao = np.array([2, 4, 1])

preco = np.array([5, 4.5, 5.5])

receita = np.dot(producao, preco)

print("Produção:", producao)
print("Preço:", preco)
print("Receita total:", receita)