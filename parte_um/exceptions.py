class MudancaEstadoError(Exception):
    def __init__(self, message=""):
        msg = "Não foi possível completar a mudança de estado. Verifique a ordem dos estados"
        self.msg = message or msg
        super(MudancaEstadoError, self).__init__(self.msg)


class DescontoError(Exception):
    def __init__(self, message=""):
        msg = "Desconto ja aplicado para este orçamento!"
        self.msg = message or msg
        super(DescontoError, self).__init__(self.msg)
