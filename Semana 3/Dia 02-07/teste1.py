# Importando bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    """Função de ativação Sigmoid"""
    return 1 / (1 + np.exp(-z))

# Valores simulados para risco
risco = np.linspace(-5, 2, 100)  # Mais pontos para suavizar a curva
probabilidade = sigmoid(risco)

# Plotando o gráfico
plt.figure(figsize=(8, 5))
plt.plot(risco, probabilidade, label='Sigmoid', color='green')
plt.title('Probabilidade de Queimada vs. Risco')
plt.xlabel('Risco de Queimada')
plt.ylabel('Probabilidade')
plt.grid(True)
plt.legend()
plt.axhline(0.5, color='red', linestyle='--', label='Limiar de 50%')
plt.legend()
plt.show()
