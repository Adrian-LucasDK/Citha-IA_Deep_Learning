import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Silencia logs informativos do TensorFlow

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# Dados simulados: temperatura em °C, nível de poluição (0 a 100)
# Saída: 0 = dia bom, 1 = dia ruim

# Variáveis de entrada
x = np.array([[30, 70], [32, 80], [28, 40], [29, 35], [34, 90]])
y = np.array([[1], [1], [0], [0], [1]]) 

# Criando o modelo
model = Sequential([
    Input(shape=(2,)),                    # Substitui input_dim e evita o aviso
    Dense(4, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compilando e treinando o modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x, y, epochs=50, verbose=0)

# Teste com novos dados
novos_dados = np.array([[31, 60], [27, 30]])

# Fazer predições   
predicoes = model.predict(novos_dados)

# Interpretação dos resultados
for i, pred in enumerate(predicoes):
    if pred >= 0.5:
        print(f"Dia {i+1}: Dia ruim (Poluição: {novos_dados[i][1]}%, Temperatura: {novos_dados[i][0]}°C)")
    else:
        print(f"Dia {i+1}: Dia bom (Poluição: {novos_dados[i][1]}%, Temperatura: {novos_dados[i][0]}°C)")
