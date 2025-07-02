import numpy as np # Importa a biblioteca NumPy para operações com arrays e álgebra linear

#Funções de ativação
# Função de ativação step: retorna 1 se z >= 0, senão retorna 0
def step(z): 
    return 1 if z >= 0 else 0 
    
# Função de ativação sigmoid: retorna o valor da função sigmoide aplicada a z
def sigmoid(z): 
    return 1 / (1 + np.exp(-z))

# Função de ativação tanh: retorna o valor da função tangente hiperbólica aplicada a z
def tanh(z): 
    return np.tanh(z)

# Função de ativação ReLU (Rectified Linear Unit): retorna z se z > 0, senão retorna 0
def relu(z): 
    return np.maximum(0, z)

#Neurônio Simples
def neuronio(x, w, b, funcao_ativacao): # Define a função do neurônio que recebe entradas, pesos, bias e uma função de ativação
    z = np.dot(x, w) + b  # Calcula a soma ponderada das entradas e pesos, adicionando o bias
    return funcao_ativacao(z)  # Aplica a função de ativação ao resultado

#Exemplo de uso
x_input = np.array([1, 1])  # Entradas do neurônio
weights = np.array([0.4, 0.6])  # Pesos do neurônio
bias = 0.1  # Bias do neurônio

print("Entradas:", x_input, "Pesos:", weights, "Bias:", bias) # Exibe as entradas, pesos e bias
print("Soma ponderada (z):", np.dot(x_input, weights) + bias) # Exibe a soma ponderada # z = 0.4*0.5 + (-0.6)*0.8 + 0.1 = -0.18
print("-" * 30) # Linha de separação para melhor visualização
print("Saída com função de ativação step:", neuronio(x_input, weights, bias, step)) # Exibe a saída do neurônio com a função de ativação step
print("Saída com função de ativação sigmoid:", neuronio(x_input, weights, bias, sigmoid)) # Exibe a saída do neurônio com a função de ativação sigmoid
print("Saída com função de ativação tanh:", neuronio(x_input, weights, bias, tanh)) # Exibe a saída do neurônio com a função de ativação tanh
print("Saída com função de ativação ReLU:", neuronio(x_input, weights, bias, relu)) # Exibe a saída do neurônio com a função de ativação ReLU
