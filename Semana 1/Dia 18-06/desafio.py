# Função para adicionar uma tarefa à lista
def adicionar_tarefa(tarefas):
    # Solicita ao usuário que digite a tarefa
    tarefa = input("Digite a tarefa a ser adicionada: ").strip()
    # Converte a tarefa para minúsculas para padronizar as comparações
    tarefa_formatada = tarefa.lower()

    # Verifica se a tarefa já existe na lista (ignorando maiúsculas/minúsculas)
    if tarefa_formatada in [t.lower() for t in tarefas]:
        print(f"A tarefa '{tarefa}' já está na lista.")
    else:
        # Adiciona a tarefa como o usuário digitou (mantém a formatação original)
        tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")

# Função para remover uma tarefa da lista
def remover_tarefa(tarefas):
    # Verifica se a lista está vazia
    if not tarefas:
        print("Nenhuma tarefa para remover.")
        return

    # Solicita ao usuário a tarefa a ser removida
    tarefa = input("Digite a tarefa a ser removida: ").strip().lower()

    # Procura a tarefa na lista, ignorando maiúsculas/minúsculas
    for t in tarefas:
        if t.lower() == tarefa:
            tarefas.remove(t)
            print(f"Tarefa '{t}' removida com sucesso!")
            return

    # Caso a tarefa não seja encontrada
    print(f"Tarefa '{tarefa}' não encontrada na lista.")

# Função para exibir todas as tarefas pendentes
def exibir_tarefas(tarefas):
    # Verifica se há tarefas na lista
    if not tarefas:
        print("Nenhuma tarefa pendente.")
    else:
        print("Tarefas pendentes:")
        # Exibe cada tarefa da lista
        for tarefa in tarefas:
            print(f"- {tarefa}")

# Função que exibe o menu de opções
def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Exibir tarefas pendentes")
    print("4. Sair")

# Função principal do programa
def main():
    # Inicializa a lista de tarefas vazia
    tarefas = []

    # Loop principal do programa, continua executando até o usuário escolher sair
    while True:
        # Mostra o menu de opções
        exibir_menu()
        # Solicita a escolha do usuário
        escolha = input("Escolha uma opção: ")

        # Verifica a opção e chama a função correspondente
        if escolha == '1':
            adicionar_tarefa(tarefas)
        elif escolha == '2':
            remover_tarefa(tarefas)
        elif escolha == '3':
            exibir_tarefas(tarefas)
        elif escolha == '4':
            print("Saindo do programa. Até logo!")
            break  # Encerra o programa
        else:
            # Caso a opção digitada não seja válida
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
