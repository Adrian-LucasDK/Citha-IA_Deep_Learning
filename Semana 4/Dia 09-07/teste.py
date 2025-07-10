import os # Importando a biblioteca OS para manipulação de variáveis de ambiente
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Silencia logs informativos do TensorFlow
import warnings # Importando a biblioteca de avisos para controlar os avisos exibidos
warnings.filterwarnings("ignore", category=UserWarning) # Ignora avisos de usuário do TensorFlow
import numpy as np #Importando a biblioteca NumPy para manipulação de arrays
import tensorflow as tf #Importando o TensorFlow para criação e treinamento de modelos de aprendizado de máquina 
from tensorflow.keras.models import Sequential #Importando o módulo Sequential do Keras para criar modelos sequenciais # type: ignore
from tensorflow.keras.layers import SimpleRNN, Dense #Importando as camadas SimpleRNN e Dense do Keras para construir a rede neural recorrente # type: ignore
from sklearn.model_selection import train_test_split #Importando a função train_test_split do scikit-learn para dividir os dados em conjuntos de treino e teste # type: ignore
import matplotlib.pyplot as plt #Importando o matplotlib para visualização de dados

#Simulação de Dados Climaticos do Norte do Brasil

num_samples = 1000  # Número de amostras
sequence_length = 7  # Comprimento da sequência
features = 3  # Número de características (chuva, temperatura, umidade)

X = np.random.rand(num_samples, sequence_length, features)  # Dados de entrada aleatórios

labels = (X[:, :, 1].mean(axis=1) > 0.5).astype(int)  # Rótulos baseados na média da temperatura

x_train, x_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=12)  # Dividindo os dados em treino e teste

model = Sequential() # Criando um modelo sequencial

model.add(SimpleRNN(32, input_shape=(sequence_length, features), activation='tanh'))  # Adicionando uma camada RNN com 32 unidades e função de ativação tanh

model.add(Dense(1, activation='sigmoid'))  # Adicionando uma camada densa de saída com ativação sigmoide

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  # Compilando o modelo com otimizador Adam e perda de entropia cruzada binária

history = model.fit(x_train, y_train, epochs=15, batch_size=16, validation_split=0.2)  # Treinando o modelo com os dados de treino

plt.figure(figsize=(12, 5)) # Configurando o tamanho da figura para o gráfico

#Grafico de Acurácia
plt.subplot(1, 2, 1)  # Criando o primeiro subplot
plt.plot(history.history['accuracy'], label='Treinamento')  # Plotando a acurácia de treino
plt.plot(history.history['val_accuracy'], label='Validação')  # Plotando a acurácia de validação
plt.title('Acurácia de Treinamento')  # Título do gráfico
plt.xlabel('Épocas')  # Rótulo do eixo x
plt.ylabel('Acurácia')  # Rótulo do eixo y
plt.legend()  # Adicionando legenda

#Grafico de Perda
plt.subplot(1, 2, 2)  # Criando o segundo subplot
plt.plot(history.history['loss'], label='Treinamento')  # Plotando a perda de treino
plt.plot(history.history['val_loss'], label='Validação')  # Plotando a perda de validação
plt.title('Perda do Treinamento')  # Título do gráfico
plt.xlabel('Épocas')  # Rótulo do eixo x
plt.ylabel('Loss')  # Rótulo do eixo y
plt.legend()  # Adicionando legenda

plt.tight_layout()  # Ajustando o layout para evitar sobreposição
plt.show() # Exibindo os gráficos