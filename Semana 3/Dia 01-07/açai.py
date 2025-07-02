import numpy as np

def reLU(z):
    """Função de ativação ReLU (Rectified Linear Unit)"""
    return np.maximum(0, z)

#Dados Simulados para produção de Açaí
producao_acai = np.array([12, -5, 8, -2, 15, 0])

saida = reLU(producao_acai)

print("Produção de Açaí:", producao_acai)
print("Saída após ReLU:", saida)