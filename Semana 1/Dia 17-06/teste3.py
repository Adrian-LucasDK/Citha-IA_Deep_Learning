# Classificação de um número inteiro como positivo, negativo, par ou ímpar
# Recebendo um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Verificando se o número é positivo, negativo ou zero e se é par ou ímpar
if numero == 0:
    classificacao = "Zero"
elif numero > 0:
    if numero % 2 == 0:
        classificacao = "Positivo e par"
    else:
        classificacao = "Positivo e ímpar"
else:
    if numero % 2 == 0:
        classificacao = "Negativo e par"
    else:
        classificacao = "Negativo e ímpar"

# Exibindo a classificação do número
print(f"O número {numero} é classificado como: {classificacao}.")
