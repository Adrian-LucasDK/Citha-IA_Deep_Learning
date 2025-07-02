import numpy as np

def tanH(z):
    """Função de ativação tangente hiperbólica"""
    return np.tanh(z)

#Niveis do rio em Metros

nivel_rio = np.array([20, 15, 25, 17, 30, 18, 20, 23, 10, 12])

previsao = tanH(nivel_rio)

print("Níveis do Rio:", nivel_rio)
print("Previsão de Cheias (tanh):", previsao)
