# Solicita o nome da pessoa
nome = input("Digite o seu nome: ")

# Solicita o sexo da pessoa (esperado 'M' ou 'F')
sexo = input("Digite o seu sexo (M ou F): ")

# Solicita o estado civil da pessoa
estado_civil = input("Digite seu estado civil (SOLTEIRA, CASADA, DIVORCIADA, etc): ")

# Converte sexo e estado civil para letras maiúsculas para evitar erros de digitação
sexo = sexo.upper()
estado_civil = estado_civil.upper()

# Verifica se o sexo é feminino e se o estado civil é casada
if sexo == "F" and estado_civil == "CASADA":
    # Se for casada e do sexo feminino, solicita o tempo de casada
    tempo = int(input("Há quantos anos você está casada? "))
    print(f"{nome}, você está casada há {tempo} anos.")
else:
    # Caso não seja mulher casada, apenas exibe os dados informados
    print(f"{nome}, seus dados foram registrados com sucesso.")
