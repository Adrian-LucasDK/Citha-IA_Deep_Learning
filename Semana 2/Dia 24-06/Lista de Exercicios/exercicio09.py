# Solicita a altura da pessoa (em metros)
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

# Solicita o sexo da pessoa (esperado 'M' para homem ou 'F' para mulher)
sexo = input("Digite seu sexo (M para masculino, F para feminino): ")

# Converte o sexo para maiúscula para evitar erros de digitação
sexo = sexo.upper()

# Verifica se o sexo é masculino
if sexo == "M":
    # Calcula o peso ideal para homens usando a fórmula
    peso_ideal = (72.7 * altura) - 58
    print(f"Peso ideal para homem: {peso_ideal:.2f} kg")
# Verifica se o sexo é feminino
elif sexo == "F":
    # Calcula o peso ideal para mulheres usando a fórmula
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Peso ideal para mulher: {peso_ideal:.2f} kg")
else:
    # Caso o sexo informado não seja válido
    print("Sexo inválido! Digite 'M' para masculino ou 'F' para feminino.")
