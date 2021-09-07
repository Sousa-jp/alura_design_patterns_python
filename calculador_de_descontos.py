from descontos import DescontoCincoItens, DescontoMaisDeQuinhentosReais, SemDesconto
from orcamento import Orcamento, Item


class CalculadorDescontos:
    @staticmethod
    def calcula(orcamento: Orcamento) -> float:
        desconto: float = DescontoCincoItens(
            DescontoMaisDeQuinhentosReais(
                SemDesconto()
            )
        ).calcula(orcamento)
        return desconto

if __name__ == '__main__':
    orcamento_1 = Orcamento()
    orcamento_1.adiciona_item(Item("ITEM-1", 100))
    orcamento_1.adiciona_item(Item("ITEM-2", 50))
    orcamento_1.adiciona_item(Item("ITEM-3", 400))

    calculador = CalculadorDescontos()

    descontos = calculador.calcula(orcamento_1)

    print(f'desconto calculado {descontos}')
