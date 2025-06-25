# Solicita o primeiro valor booleano ao usuário (esperado: True ou False)
valor1 = input("Digite o primeiro valor lógico (True ou False): ")

# Converte a string digitada para valor booleano real
valor1 = valor1.strip().capitalize() == "True"

# Solicita o segundo valor booleano ao usuário (esperado: True ou False)
valor2 = input("Digite o segundo valor lógico (True ou False): ")

# Converte a string digitada para valor booleano real
valor2 = valor2.strip().capitalize() == "True"

# Verifica se os dois valores são verdadeiros
if valor1 and valor2:
    print("Ambos os valores são VERDADEIROS.")
# Verifica se os dois valores são falsos
elif not valor1 and not valor2:
    print("Ambos os valores são FALSOS.")
# Caso contrário, são diferentes
else:
    print("Os valores são diferentes (um verdadeiro e outro falso).")
