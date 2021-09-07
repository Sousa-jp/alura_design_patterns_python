from impostos import ICMS, ISS


class CalculadorImpostos(object):
    @staticmethod
    def realiza_calculo(orcamento, imposto) -> None:
        imposto_calculado: float = imposto.calcula(orcamento)
        print(imposto_calculado)

if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = CalculadorImpostos()
    orcamento_1 = Orcamento(500)

    calculador.realiza_calculo(orcamento_1, ISS)
    calculador.realiza_calculo(orcamento_1, ICMS)
