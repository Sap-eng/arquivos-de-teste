import json

ARQUIVO = "tarefas.json"

# carregar tarefas do arquivo
def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []

# salvar tarefas no arquivo
def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

def mostrar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa encontrada.")
        return

    print("\n📋 Suas tarefas:")
    for i, t in enumerate(tarefas):
        status = "✔" if t["concluida"] else "❌"
        print(f"{i + 1}. {t['nome']} [{status}]")

def adicionar_tarefa(tarefas):
    nome = input("Digite a tarefa: ")
    tarefas.append({"nome": nome, "concluida": False})
    print("Tarefa adicionada!")

def concluir_tarefa(tarefas):
    mostrar_tarefas(tarefas)
    i = int(input("Número da tarefa concluída: ")) - 1

    if 0 <= i < len(tarefas):
        tarefas[i]["concluida"] = True
        print("Tarefa marcada como concluída!")

def remover_tarefa(tarefas):
    mostrar_tarefas(tarefas)
    i = int(input("Número da tarefa para remover: ")) - 1

    if 0 <= i < len(tarefas):
        tarefas.pop(i)
        print("Tarefa removida!")

def menu():
    tarefas = carregar_tarefas()

    while True:
        print("\n==== TO-DO LIST ====")
        print("1 - Adicionar tarefa")
        print("2 - Ver tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)

        elif opcao == "2":
            mostrar_tarefas(tarefas)

        elif opcao == "3":
            concluir_tarefa(tarefas)

        elif opcao == "4":
            remover_tarefa(tarefas)

        elif opcao == "5":
            salvar_tarefas(tarefas)
            print("Salvando e saindo...")
            break

        else:
            print("Opção inválida")

        salvar_tarefas(tarefas)

menu()