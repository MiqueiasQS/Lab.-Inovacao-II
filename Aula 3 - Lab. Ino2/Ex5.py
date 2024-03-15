from abc import ABC, abstractmethod
from datetime import datetime

class Veiculo(ABC):
    def __init__(self, modelo, ano, placa, preco_por_dia):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.preco_por_dia = preco_por_dia

    @abstractmethod
    def calcular_aluguel(self, dias: int) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.modelo} ({self.ano}) - Placa: {self.placa}"

class Carro(Veiculo):
    def calcular_aluguel(self, dias: int) -> float:
        return self.preco_por_dia * dias

class Moto(Veiculo):
    def calcular_aluguel(self, dias: int) -> float:
        return self.preco_por_dia * dias

class Caminhao(Veiculo):
    def calcular_aluguel(self, dias: int) -> float:
        return self.preco_por_dia * dias

class SistemaAluguel:
    veiculos = []

    @staticmethod
    def adicionar_veiculo(veiculo: Veiculo):
        SistemaAluguel.veiculos.append(veiculo)

    @staticmethod
    def listar_veiculos_disponiveis():
        for veiculo in SistemaAluguel.veiculos:
            print(veiculo)

    @staticmethod
    def encontrar_veiculos_disponiveis(data: datetime):
        veiculos_disponiveis = []
        for veiculo in SistemaAluguel.veiculos:
            veiculos_disponiveis.append(veiculo)
        return veiculos_disponiveis

def menu():
    print("1. Adicionar veículo")
    print("2. Listar veículos disponíveis")
    print("3. Encontrar veículos disponíveis para aluguel em uma data")
    print("4. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tipo_veiculo = input("Digite o tipo de veículo (carro, moto, caminhao): ")
            modelo = input("Digite o modelo do veículo: ")
            ano = input("Digite o ano do veículo: ")
            placa = input("Digite a placa do veículo: ")
            preco_por_dia = float(input("Digite o preço de aluguel por dia do veículo: "))

            if tipo_veiculo.lower() == 'carro':
                veiculo = Carro(modelo, ano, placa, preco_por_dia)
            elif tipo_veiculo.lower() == 'moto':
                veiculo = Moto(modelo, ano, placa, preco_por_dia)
            elif tipo_veiculo.lower() == 'caminhao':
                veiculo = Caminhao(modelo, ano, placa, preco_por_dia)
            else:
                print("Tipo de veículo inválido!")
                continue

            SistemaAluguel.adicionar_veiculo(veiculo)
            print("Veículo adicionado com sucesso!")

        elif opcao == '2':
            print("Veículos disponíveis para aluguel:")
            SistemaAluguel.listar_veiculos_disponiveis()

        elif opcao == '3':
            data = input("Digite a data para verificar a disponibilidade (formato: AAAA-MM-DD): ")
            try:
                data = datetime.strptime(data, "%Y-%m-%d")
                veiculos_disponiveis = SistemaAluguel.encontrar_veiculos_disponiveis(data)
                print("Veículos disponíveis para aluguel nesta data:")
                for veiculo in veiculos_disponiveis:
                    print(veiculo)
            except ValueError:
                print("Formato de data inválido!")

        elif opcao == '4':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
