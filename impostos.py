
class ISS:
    @staticmethod
    def calcula(orcamento) -> float:
        return orcamento.valor * 0.1


class ICMS:
    @staticmethod
    def calcula(orcamento) -> float:
        return orcamento.valor * 0.06


if __name__ == '__main__':
    pass
