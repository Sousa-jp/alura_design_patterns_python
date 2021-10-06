from orcamento import Orcamento


class DescontoCincoItens:
    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento: Orcamento) -> float:
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return self.__proximo_desconto.calcula(orcamento)


class DescontoMaisDeQuinhentosReais:
    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento: Orcamento) -> float:
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self.__proximo_desconto.calcula(orcamento)


class SemDesconto:
    @staticmethod
    def calcula(orcamento: Orcamento) -> int:
        return 0*orcamento
