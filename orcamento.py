
class Orcamento(object):
    def __init__(self, valor: float):
        self.__valor: float = valor

    @property
    def valor(self) -> float:
        return self.__valor

if __name__ == '__main__':
    orcamento = Orcamento(500)
    valor_orcamento = orcamento.valor