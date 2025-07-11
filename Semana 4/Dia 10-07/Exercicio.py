import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import SimpleRNN, Dense   # type: ignore
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Simulação de Dados de Movimento de Peixes no Rio Amazonas
num_samples = 1000  # Número total de amostras
sequence_length = 24  # 24 horas de monitoramento
features = 3  # Velocidade, profundidade, frequência de viradas

# Criando dados aleatórios simulados
X = np.random.rand(num_samples, sequence_length, features)

# Criando rótulos: anomalias se a média da frequência de viradas + variação de velocidade for alta
frequencia_mudancas = X[:, :, 2].mean(axis=1)
variabilidade_velocidade = X[:, :, 0].std(axis=1)

# Critério simples para gerar anomalias: se algum padrão for incomum
labels = ((frequencia_mudancas > 0.6) | (variabilidade_velocidade > 0.25)).astype(int)

# Dividindo dados em treino e teste
x_train, x_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Criando a rede RNN
model = Sequential()
model.add(SimpleRNN(32, input_shape=(sequence_length, features), activation='tanh'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Treinamento do modelo
history = model.fit(x_train, y_train, epochs=15, batch_size=16, validation_split=0.2)

# Visualização dos resultados
plt.figure(figsize=(12, 5))

# Acurácia
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Treinamento')
plt.plot(history.history['val_accuracy'], label='Validação')
plt.title('Acurácia de Treinamento')
plt.xlabel('Épocas')
plt.ylabel('Acurácia')
plt.legend()

# Perda
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Treinamento')
plt.plot(history.history['val_loss'], label='Validação')
plt.title('Perda do Treinamento')
plt.xlabel('Épocas')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()
