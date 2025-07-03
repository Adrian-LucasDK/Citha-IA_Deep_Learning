#Importando bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt

# Função de custo para um modelo de regressão linear simples
def funcao_custo (peso, dado_entrada, dado_saida_real):
    predicao = dado_entrada * peso  # Calcula a predição do modelo
    erro = dado_saida_real - predicao  # Calcula o erro entre a predição
    return erro

def gradiente_funcao_custo(peso, dado_entrada, dado_saida_real):
    predicao = dado_entrada * peso  # Calcula a predição do modelo
    derivada = 2 *(predicao - dado_saida_real) * dado_entrada  # Calcula a derivada da função de custo
    return derivada  # Retorna a média da derivada

# Dados de entrada e saída para o modelo
peso_inicial = 0.5  # Peso inicial do modelo
taxa_aprendizado = 0.01  # Taxa de aprendizado para o algoritmo de otimização
dado_entrada = 10 # Dados de entrada
dado_saida_real = 20  # Dados de saída real

print(f"\nPeso Inicial: {peso_inicial:.2f}")
print(f"Custo final: {funcao_custo(peso_inicial, dado_entrada, dado_saida_real):.2f}")