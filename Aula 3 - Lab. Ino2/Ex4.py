import csv
import os

class GerenciadorDeProdutos:
    def __init__(self, arquivo='produtos.csv'):
        self.arquivo = arquivo
        self.produtos = {}
        self.carregar_produtos()

    def carregar_produtos(self):
        if not os.path.exists(self.arquivo):
            return
        with open(self.arquivo, mode='r', newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                self.produtos[linha['nome']] = {'preco': float(linha['preco']), 'quantidade': int(linha['quantidade'])}

    def salvar_produtos(self):
        with open(self.arquivo, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=['nome', 'preco', 'quantidade'])
            escritor.writeheader()
            for nome, dados in self.produtos.items():
                escritor.writerow({'nome': nome, 'preco': dados['preco'], 'quantidade': dados['quantidade']})

    def adicionar_produto(self, nome, preco, quantidade):
        self.produtos[nome] = {'preco': preco, 'quantidade': quantidade}
        self.salvar_produtos()

    def atualizar_produto(self, nome, preco=None, quantidade=None):
        if nome not in self.produtos:
            print("Produto não encontrado.")
            return
        if preco is not None:
            self.produtos[nome]['preco'] = preco
        if quantidade is not None:
            self.produtos[nome]['quantidade'] = quantidade
        self.salvar_produtos()

    def remover_produto(self, nome):
        if nome in self.produtos:
            del self.produtos[nome]
            self.salvar_produtos()
        else:
            print("Produto não encontrado.")

    def mostrar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return
        print("Produtos disponíveis:")
        for nome, dados in self.produtos.items():
            print(f"{nome} - Preço: R${dados['preco']:.2f}, Quantidade: {dados['quantidade']}")

############## TESTES ##############
# gerenciador = GerenciadorDeProdutos()
# gerenciador.adicionar_produto('Caneta', 1.50, 100)
# gerenciador.atualizar_produto('Caneta', quantidade=150)
# gerenciador.mostrar_produtos()
# gerenciador.remover_produto('Caneta')
