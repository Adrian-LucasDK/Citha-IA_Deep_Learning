# Solicita o número de identificação do aluno
numero = input("Digite o número de identificação do aluno: ")

# Solicita as 3 notas das verificações
nota1 = float(input("Digite a nota da 1ª verificação: "))
nota2 = float(input("Digite a nota da 2ª verificação: "))
nota3 = float(input("Digite a nota da 3ª verificação: "))

# Solicita a média dos exercícios
media_exercicios = float(input("Digite a média dos exercícios: "))

# Calcula a média de aproveitamento usando a fórmula
media_aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7

# Exibe os dados coletados e a média de aproveitamento
print(f"\nNúmero do aluno: {numero}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média dos exercícios: {media_exercicios}")
print(f"Média de aproveitamento: {media_aproveitamento:.2f}")

# Define o conceito com base na média de aproveitamento
if media_aproveitamento >= 90:
    conceito = "A"
    mensagem = "Aprovado"
elif media_aproveitamento >= 75:
    conceito = "B"
    mensagem = "Aprovado"
elif media_aproveitamento >= 60:
    conceito = "C"
    mensagem = "Aprovado"
elif media_aproveitamento >= 40:
    conceito = "D"
    mensagem = "Reprovado"
else:
    conceito = "E"
    mensagem = "Reprovado"

# Exibe o conceito e a mensagem final
print(f"Conceito: {conceito}")
print(f"Situação: {mensagem}")
