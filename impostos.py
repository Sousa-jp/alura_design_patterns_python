from abc import ABCMeta, abstractmethod

from orcamento import Orcamento


class TemplateImpostoCondicional(metaclass=ABCMeta):
    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        ...

    @staticmethod
    @abstractmethod
    def maxima_taxacao(orcamento):
        ...

    @staticmethod
    @abstractmethod
    def minima_taxacao(orcamento):
        ...


class ISS:
    @staticmethod
    def calcula(orcamento: Orcamento) -> float:
        return orcamento.valor * 0.1


class ICMS:
    @staticmethod
    def calcula(orcamento: Orcamento) -> float:
        return orcamento.valor * 0.06


class ICPP(TemplateImpostoCondicional):
    def deve_usar_maxima_taxacao(self, orcamento) -> bool:
        return orcamento.valor > 500

    @staticmethod
    def maxima_taxacao(orcamento) -> float:
        return orcamento.valor * 0.07

    @staticmethod
    def minima_taxacao(orcamento) -> float:
        return orcamento.valor * 0.05


class IKCV(TemplateImpostoCondicional):
    def deve_usar_maxima_taxacao(self, orcamento) -> bool:
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    @staticmethod
    def maxima_taxacao(orcamento) -> float:
        return orcamento.valr * 0.1

    @staticmethod
    def minima_taxacao(orcamento) -> float:
        return orcamento.valor * 0.06

    @staticmethod
    def __tem_item_maior_que_100_reais(orcamento: Orcamento) -> bool:
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False

if __name__ == '__main__':
    pass
