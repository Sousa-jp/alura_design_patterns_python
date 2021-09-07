from typing import Union

from impostos import ICMS, ISS
from orcamento import Orcamento


class CalculadorImpostos:
    @staticmethod
    def realiza_calculo(orcamento: Orcamento, imposto: Union[ICMS, ISS]) -> None:
        imposto_calculado: float = imposto.calcula(orcamento)
        print(imposto_calculado)

if __name__ == '__main__':
    calculador = CalculadorImpostos()
    orcamento_1 = Orcamento()

    calculador.realiza_calculo(orcamento_1, ISS())
    calculador.realiza_calculo(orcamento_1, ICMS())
