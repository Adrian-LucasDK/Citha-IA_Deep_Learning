#Recebendo as váriaveis do usuário para o IMC
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

#verificaçãos e o número é positivo e maior que zero
if peso <= 0 or altura <= 0:
    print("Peso e altura devem ser números positivos e maiores que zero.")
    exit()
    
# Calculando o IMC
imc = peso / (altura ** 2)

# Verificando a classificação do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
elif 30 <= imc < 34.9:
    classificacao = "Obesidade grau 1"
elif 35 <= imc < 39.9:
    classificacao = "Obesidade grau 2"
elif imc >= 40:
    classificacao = "Obesidade grau 3"
else:
    classificacao = "Classificação desconhecida"

# Exibindo as informações do usuário
print(f"\nSeu peso é {peso} kg e sua altura é {altura} m.")

# Exibindo a classificação do IMC
print(f"Classificação do IMC: {classificacao}")

# Exibindo o resultado
print(f"Seu IMC é {imc:.1f}.")