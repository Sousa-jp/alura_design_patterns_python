from datetime import date
from typing import List


class Item:
    def __init__(self, descricao: str, valor: float):
        self._descricao: str = descricao
        self._valor: float = valor

    @property
    def descricao(self) -> str:
        return self._descricao

    @property
    def valor(self) -> float:
        return self._valor


class NotaFiscal:
    def __init__(self, razao_social: str,
                 cnpj: str,
                 itens: List[Item],
                 data_da_emissao: date = date.today(), detalhes: str = ''):
        """"""
        self._razao_social: str = razao_social
        self._cnpj: str = cnpj
        self._data_emissao: date = data_da_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')
        self._detalhes: str = detalhes
        self._itens: List[Item] = itens

    @property
    def razao_social(self) -> str:
        return self._razao_social

    @property
    def cnpj(self) -> str:
        return self._cnpj

    @property
    def data_emissao(self) -> date:
        return self._data_emissao

    @property
    def detalhes(self) -> str:
        return self._detalhes


if __name__ == '__main__':
    from criador_nota_fiscal import BuilderNotaFiscal

    itens_teste: List[Item] = [
        Item(
            'ITEM A',
            100
        ),
        Item(
            'ITEM B',
            200
        )
    ]

    nota_fiscal: NotaFiscal = NotaFiscal(
        razao_social='FHSA Limitada',
        cnpj='012345678901234',
        itens=itens_teste,
    )

    nota_fiscal_gerada_builder = (
        BuilderNotaFiscal()
        .com_razao_social('FHSA Limitada')
        .com_cnpj('012345678901234')
        .com_itens(itens_teste)
        .controi()
    )
