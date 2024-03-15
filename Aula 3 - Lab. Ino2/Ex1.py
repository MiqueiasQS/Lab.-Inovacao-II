class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tarefa '{task}' adicionada com sucesso!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Tarefa '{task}' removida com sucesso!")
        else:
            print("Tarefa não encontrada.")

    def show_tasks(self):
        if self.tasks:
            print("Tarefas:")
            for task in self.tasks:
                print(f"- {task}")
        else:
            print("A lista de tarefas está vazia.")

    def clear_tasks(self):
        self.tasks.clear()
        print("Lista de tarefas limpa com sucesso!")

def main():
    todo_list = TodoList()
    while True:
        print("\nMenu:")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Mostrar Tarefas")
        print("4. Limpar Lista de Tarefas")
        print("5. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            task = input("Digite a tarefa a ser adicionada: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Digite a tarefa a ser removida: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            todo_list.clear_tasks()
        elif choice == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
