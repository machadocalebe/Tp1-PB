from datetime import datetime


tarefas = []

def gerar_id():
    return len(tarefas) + 1

def adicionar_tarefa(descricao, prazo_final, urgencia):
    """
    Adiciona uma nova tarefa à lista de tarefas.

    Parâmetros:
    descricao (str): Descrição da tarefa.
    prazo_final (str): Data limite para concluir a tarefa (formato: DD/MM/AAAA).
    urgencia (str): Nível de urgência da tarefa (Baixa, Média, Alta).

    Retorna:
    None
    """
    nova_tarefa = {
        "ID": gerar_id(),
        "Descrição": descricao,
        "Data de Criação": datetime.now().strftime("%d/%m/%Y"),
        "Status": "Pendente",
        "Prazo Final": prazo_final,
        "Urgência": urgencia
    }
    tarefas.append(nova_tarefa)
    print("\nTarefa adicionada com sucesso!")

def listar_tarefas():
    """
    Exibe todas as tarefas na lista.

    Retorna:
    None
    """
    if not tarefas:
        print("\nNão há tarefas pendentes.")
        return
    
    print("\nLista de Tarefas:")
    for tarefa in tarefas:
        print(f"ID: {tarefa['ID']}, Descrição: {tarefa['Descrição']}, "
              f"Data de Criação: {tarefa['Data de Criação']}, Status: {tarefa['Status']}, "
              f"Prazo: {tarefa['Prazo Final']}, Urgência: {tarefa['Urgência']}")

def marcar_concluida(tarefa_id):
    """
    Marca uma tarefa específica como concluída.

    Parâmetros:
    tarefa_id (int): ID da tarefa a ser marcada como concluída.

    Retorna:
    None
    """
    for tarefa in tarefas:
        if tarefa["ID"] == tarefa_id:
            tarefa["Status"] = "Concluída"
            print("\nTarefa marcada como concluída!")
            return
    print("\nTarefa não encontrada!")

def remover_tarefa(tarefa_id):
    """
    Remove uma tarefa da lista.

    Parâmetros:
    tarefa_id (int): ID da tarefa a ser removida.

    Retorna:
    None
    """
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa["ID"] != tarefa_id]
    print("\nTarefa removida com sucesso!")

def menu():
    """
    Exibe o menu de opções e processa as operações com base na escolha do usuário.

    Retorna:
    None
    """
    while True:
        print("\n--- Sistema de Gestão de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            descricao = input("Descrição da tarefa: ")
            prazo_final = input("Prazo final (DD/MM/AAAA): ")
            urgencia = input("Nível de urgência (Baixa, Média, Alta): ")
            adicionar_tarefa(descricao, prazo_final, urgencia)
        
        elif opcao == "2":
            listar_tarefas()
        
        elif opcao == "3":
            try:
                tarefa_id = int(input("ID da tarefa a ser marcada como concluída: "))
                marcar_concluida(tarefa_id)
            except ValueError:
                print("Por favor, insira um número válido.")
        
        elif opcao == "4":
            try:
                tarefa_id = int(input("ID da tarefa a ser removida: "))
                remover_tarefa(tarefa_id)
            except ValueError:
                print("Por favor, insira um número válido.")
        
        elif opcao == "5":
            print("Saindo do sistema... Até logo!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

menu()
