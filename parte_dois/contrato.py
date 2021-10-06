from datetime import date
from typing import List


class Contrato:
    def __init__(self, data, cliente, tipo):
        self._data: date = data
        self._cliente: str = cliente
        self._tipo: str = tipo

    @property
    def data(self) -> date:
        return self._data

    @data.setter
    def data(self, data) -> None:
        self._data = data

    @property
    def cliente(self) -> str:
        return self._cliente

    @cliente.setter
    def cliente(self, cliente) -> None:
        self._cliente = cliente

    @property
    def tipo(self) -> str:
        return self._tipo

    @tipo.setter
    def tipo(self, tipo) -> None:
        self._tipo = tipo

    def avanca(self) -> None:
        if self._tipo == 'NOVO':
            self._tipo = 'EM ANDAMENTO'
        elif self._tipo == 'EM ANDAMENTO':
            self._tipo = 'ACERTADO'
        elif self._tipo == 'ACERTADO':
            self._tipo = 'CONCLUIDO'

    def salva_estado(self):
        return Estado(Contrato(
            data=self._data,
            cliente=self._cliente,
            tipo=self._tipo
        ))

    def restaura_estado(self, estado):
        self._cliente = estado.contrato.cliente
        self._data = estado.contrato.data
        self._tipo = estado.contrato.tipo


class Estado:
    def __init__(self, contrato: Contrato):
        self._contrato: Contrato = contrato

    @property
    def contrato(self):
        return self._contrato


class Historico:
    def __init__(self):
        self._estados_salvos: List[Estado] = []

    def obtem_estado(self, indice: int):
        return self._estados_salvos[indice]

    def adiciona_estado(self, estado: Estado):
        self._estados_salvos.append(estado)


if __name__ == '__main__':
    historico_teste = Historico()

    contrato = Contrato(
        data=date.today(),
        cliente='Flávio Almeida',
        tipo='NOVO'
    )
    contrato.avanca()

    historico_teste.adiciona_estado(contrato.salva_estado())

    contrato.avanca()
    contrato.cliente = "John"

    historico_teste.adiciona_estado(contrato.salva_estado())

    contrato.avanca()

    historico_teste.adiciona_estado(contrato.salva_estado())

    print(contrato.__dict__)
    contrato.restaura_estado(historico_teste.obtem_estado(1))
    print(contrato.__dict__)
