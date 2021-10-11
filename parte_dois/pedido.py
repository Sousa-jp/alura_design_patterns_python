from datetime import date
from abc import ABCMeta, abstractmethod


class Pedido:
    def __init__(self,cliente, valor):
        self._cliente = cliente
        self._valor = valor
        self._status = 'NOVO'
        self._data_finalizacao = None

    @property
    def cliente(self):
        return self._cliente

    @property
    def valor(self):
        return self._valor

    @property
    def status(self):
        return self._status

    @property
    def data_finalizacao(self):
        return self._data_finalizacao

    def paga(self):
        self._status = 'PAGO'

    def finaliza(self):
        self._data_finalizacao = date.today()
        self._status = 'ENTREGUE'


class Comando(metaclass=ABCMeta):
    @abstractmethod
    def executa(self):
        ...


class ConcluiPedidio(Comando):
    def __init__(self, pedido):
        self._pedido = pedido

    def executa(self):
        self._pedido.finaliza()


class PagaPedidio(Comando):
    def __init__(self, pedido):
        self._pedido = pedido

    def executa(self):
        self._pedido.paga()


class FilaTrabalho:
    def __init__(self):
        self._comandos = []

    def adiciona(self, comando):
        self._comandos.append(comando)

    def processa(self):
        for comando in self._comandos:
            comando.executa()


if __name__ == '__main__':

    pedido1 = Pedido("João", 100)
    pedido2 = Pedido("Pablo", 1500)

    fila_trabalho = FilaTrabalho()

    comando1 = ConcluiPedidio(pedido1)
    comando2 = PagaPedidio(pedido1)
    comando3 = ConcluiPedidio(pedido2)

    fila_trabalho.adiciona(comando1)
    fila_trabalho.adiciona(comando2)
    fila_trabalho.adiciona(comando3)

    fila_trabalho.processa()
