from typing import Union

from impostos import ICMS, ISS, ICPP, IKCV
from orcamento import Orcamento, Item

impostos = Union[ICMS, ISS, ICPP, IKCV]


class CalculadorImpostos:
    @staticmethod
    def realiza_calculo(orcamento: Orcamento, imposto: impostos) -> None:
        imposto_calculado: float = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == '__main__':
    calculador = CalculadorImpostos()

    orcamento_1 = Orcamento()
    orcamento_1.adiciona_item(Item("ITEM 1", 50))
    orcamento_1.adiciona_item(Item("ITEM 2", 200))
    orcamento_1.adiciona_item(Item("ITEM 3", 250))

    print("ISS e ICMS")
    calculador.realiza_calculo(orcamento_1, ISS())
    calculador.realiza_calculo(orcamento_1, ICMS())

    print("ISS com ICMS")
    calculador.realiza_calculo(orcamento_1, ISS(ICMS()))

    print("ICPP e IKCV")
    calculador.realiza_calculo(orcamento_1, ICPP())
    calculador.realiza_calculo(orcamento_1, IKCV())

    print("ICPP com IKCV")
    calculador.realiza_calculo(orcamento_1, ICPP(IKCV()))
