from typing import Union, List
from datetime import date

from nota_fiscal import Item, NotaFiscal


class BuilderNotaFiscal:
    def __init__(self):
        self._razao_social: Union[str, None] = None
        self._cnpj: Union[str, None] = None
        self._data_emissao: Union[date, None] = None
        self._itens: Union[List[Item], None] = None
        self._detalhes: Union[str, None] = None

    def com_razao_social(self, razao_social: str):
        self._razao_social: str = razao_social
        return self

    def com_cnpj(self, cnpj: str):
        self._cnpj: str = cnpj
        return self

    def com_data_emissao(self, data_emissao: date):
        self._data_emissao: date = data_emissao
        return self

    def com_itens(self, itens: List[Item]):
        self._itens: List[Item] = itens
        return self

    def com_detalhes(self, detalhes: str):
        self._detalhes: str = detalhes
        return self

    def controi(self) -> NotaFiscal:
        if not self._razao_social:
            raise Exception("Razão social deve ser preenchida")
        if not self._cnpj:
            raise Exception("CNPJ deve ser preenchida")
        if not self._itens:
            raise Exception("Itens deve ser preenchida")
        if not self._data_emissao:
            self._data_emissao: date = date.today()
        if not self._detalhes:
            self._detalhes: str = ''

        return NotaFiscal(
            razao_social=self._razao_social,
            cnpj=self._cnpj,
            data_da_emissao=self._data_emissao,
            itens=self._itens,
            detalhes=self._detalhes
        )
