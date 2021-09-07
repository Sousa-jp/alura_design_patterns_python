from typing import List


class Orcamento:
    def __init__(self):
        self.__itens: List[Item] = []

    @property
    def valor(self) -> float:
        total: float = 0
        for item in self.__itens:
            total += item.valor
        return total

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

if __name__ == '__main__':
    orcamento = Orcamento()
    valor_orcamento = orcamento.valor
