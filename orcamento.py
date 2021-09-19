from typing import List
from abc import ABCMeta, abstractmethod
from exceptions import MudancaEstadoError, DescontoError


class Orcamento:
    def __init__(self):
        self.__itens: List[Item] = []
        self.estado_atual = EmAprovacao()
        self.__desconto_extra = 0
        self.__aceita_desconto = True

    def aprova(self) -> None:
        self.estado_atual.aprova(self)

    def reprova(self) -> None:
        self.estado_atual.reprova(self)

    def finaliza(self) -> None:
        self.estado_atual.finaliza(self)

    def aplica_desconto_extra(self) -> None:
        if self.__aceita_desconto:
            self.estado_atual.aplica_desconto_extra(self)
            self.__aceita_desconto = False
        else:
            raise DescontoError()

    def adiciona_desconto_extra(self, desconto) -> None:
        self.__desconto_extra += desconto

    @property
    def valor(self) -> float:
        total: float = 0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    def obter_itens(self) -> tuple:
        return tuple(self.__itens)

    @property
    def total_itens(self) -> int:
        return len(self.__itens)

    def adiciona_item(self, item) -> None:
        self.__itens.append(item)


class Item:
    def __init__(self, nome: str, valor: float):
        self.__nome: str = nome
        self.__valor: float = valor

    @property
    def valor(self) -> float:
        return self.__valor

    @property
    def nome(self) -> str:
        return self.__nome


class EstadoOrcamento(metaclass=ABCMeta):

    @abstractmethod
    def aplica_desconto_extra(self, orcamento: Orcamento) -> None:
        ...

    @abstractmethod
    def aprova(self, orcamento: Orcamento) -> None:
        ...

    @abstractmethod
    def reprova(self, orcamento: Orcamento) -> None:
        ...

    @abstractmethod
    def finaliza(self, orcamento: Orcamento) -> None:
        ...


class EmAprovacao(EstadoOrcamento):

    def aplica_desconto_extra(self, orcamento: Orcamento) -> None:
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprova(self, orcamento: Orcamento) -> None:
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento: Orcamento) -> None:
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento) -> None:
        raise MudancaEstadoError('Orçamento em aprovação não podem ir para finalizado')


class Aprovado(EstadoOrcamento):

    def aplica_desconto_extra(self, orcamento: Orcamento) -> None:
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento: Orcamento) -> None:
        raise MudancaEstadoError('Orçamento já está aprovado')

    def reprova(self, orcamento: Orcamento) -> None:
        raise MudancaEstadoError('Orçamento aprovados não podem ser reprovados')

    def finaliza(self, orcamento: Orcamento) -> None:
        orcamento.estado_atual = Finalizado()


class Reprovado(EstadoOrcamento):

    def aplica_desconto_extra(self, orcamento: Orcamento) -> None:
        raise MudancaEstadoError('Orçamentos reprovados não receberam desconto extra')

    def aprova(self, orcamento: Orcamento) -> None:
        raise MudancaEstadoError('Orçamento reprovado não pode ser aprovado')

    def reprova(self, orcamento: Orcamento) -> None:
        raise MudancaEstadoError('Orçamento reprovado não pode ser reprovado novamente')

    def finaliza(self, orcamento: Orcamento) -> None:
        orcamento.estado = Finalizado()


class Finalizado(EstadoOrcamento):

    def aplica_desconto_extra(self, orcamento: Orcamento) -> None:
        raise MudancaEstadoError('Orçamentos finalizados não receberam desconto extra')

    def aprova(self, orcamento: Orcamento) -> None:
        raise MudancaEstadoError('Orçamentos finalizados não podem ser aprovados novamente')

    def reprova(self, orcamento: Orcamento) -> None:
        raise MudancaEstadoError('Orçamentos finalizados não podem ser reprovados')

    def finaliza(self, orcamento: Orcamento) -> None:
        raise MudancaEstadoError('Orçamentos finalizados não podem ser finalizados novamente')


if __name__ == '__main__':
    orcamento_1 = Orcamento()
    orcamento_1.adiciona_item(Item('ITEM - 1', 100))
    orcamento_1.adiciona_item(Item('ITEM - 2', 50))
    orcamento_1.adiciona_item(Item('ITEM - 3', 400))

    print(orcamento_1.valor)
    orcamento_1.aprova()
    orcamento_1.aplica_desconto_extra()
    print(orcamento_1.valor)

