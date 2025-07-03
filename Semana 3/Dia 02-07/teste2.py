#Importando a biblioteca NumPy
import  numpy as np

def sigmoid(z):
    """Função de ativação Sigmoid"""
    return 1 / (1 + np.exp(-z))

risco_queimada = np.linspace(-5, 2, 100)  # Valores simulados para risco de queimada
probabilidade_queimada = sigmoid(risco_queimada)  # Calcula a prob

print("Risco de Queimada:", risco_queimada)

for risco, probabilidade in zip(risco_queimada, np.round(probabilidade_queimada, 3)):
    print(f"Risco: {risco:.1f}, Probabilidade de Queimada: {probabilidade:.3f}")