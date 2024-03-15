class ListaDeCompras:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, nome, preco):
        self.itens[nome] = preco
        print(f"Item '{nome}' adicionado com sucesso!")

    def remover_item(self, nome):
        if nome in self.itens:
            del self.itens[nome]
            print(f"Item '{nome}' removido com sucesso!")
        else:
            print(f"Item '{nome}' não encontrado na lista.")

    def mostrar_itens(self):
        if self.itens:
            print("Lista de Compras:")
            for nome, preco in self.itens.items():
                print(f"{nome}: R${preco:.2f}")
        else:
            print("A lista de compras está vazia.")

    def calcular_total(self):
        total = sum(self.itens.values())
        print(f"Total de gastos: R${total:.2f}")
        return total
