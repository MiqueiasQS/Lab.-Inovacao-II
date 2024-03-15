import json

class GerenciadorDeContatos:
    def __init__(self, arquivo='contatos.json'):
        self.arquivo = arquivo
        self.carregar_contatos()

    def carregar_contatos(self):
        try:
            with open(self.arquivo, 'r') as f:
                self.contatos = json.load(f)
        except FileNotFoundError:
            self.contatos = {}

    def salvar_contatos(self):
        with open(self.arquivo, 'w') as f:
            json.dump(self.contatos, f, indent=4)

    def adicionar_contato(self, nome, telefone, email):
        self.contatos[nome] = {'telefone': telefone, 'email': email}
        self.salvar_contatos()

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            self.salvar_contatos()
        else:
            print("Contato não encontrado.")

    def buscar_contato(self, nome):
        return self.contatos.get(nome, "Contato não encontrado.")

    def mostrar_contatos(self):
        for nome, info in self.contatos.items():
            print(f"{nome}: {info}")


############## TESTES ##############
# gerenciador = GerenciadorDeContatos()
# gerenciador.adicionar_contato('Maria', '1234-5678', 'maria@email.com')
# print(gerenciador.buscar_contato('Maria'))
# gerenciador.mostrar_contatos()
# gerenciador.remover_contato('Maria')