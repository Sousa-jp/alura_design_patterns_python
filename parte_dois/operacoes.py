class Subtracao:
    def __init__(self, expressao_esquerda, expressao_direita):
        self._expressao_esquerda = expressao_esquerda
        self._expressao_direita = expressao_direita

    @property
    def expressao_esquerda(self):
        return self._expressao_esquerda

    @property
    def expressao_direita(self):
        return self._expressao_direita

    def avalia(self) -> float:
        return self._expressao_esquerda.avalia() - self._expressao_direita.avalia()

    def aceita(self, visitor):
        visitor.visita_subtracao(self)


class Soma:
    def __init__(self, expressao_esquerda, expressao_direita):
        self._expressao_esquerda = expressao_esquerda
        self._expressao_direita = expressao_direita

    @property
    def expressao_esquerda(self):
        return self._expressao_esquerda

    @property
    def expressao_direita(self):
        return self._expressao_direita

    def avalia(self) -> float:
        return self._expressao_esquerda.avalia() + self._expressao_direita.avalia()

    def aceita(self, visitor):
        visitor.visita_soma(self)


class Numero:
    def __init__(self, numero):
        self._numero = numero

    def avalia(self) -> float:
        return self._numero

    def aceita(self, visitor):
        visitor.visita_numero(self)


if __name__ == '__main__':
    from impressao import Impressao

    expressao_direita_test = Soma(Numero(10), Numero(20))
    expressao_esquerda_test = Soma(Numero(5), Numero(2))
    expressao_conta = Soma(expressao_esquerda_test, expressao_direita_test)

    impressao = Impressao()
    expressao_conta.aceita(impressao)

    print('\n--------------------------')
