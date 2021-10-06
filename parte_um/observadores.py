def imprime(nota_fiscal) -> None:
    print(f"Imprimindo nota fiscal {nota_fiscal.cnpj}")


def envia_email(nota_fiscal) -> None:
    print(f"Enviando por email nota fiscal {nota_fiscal.cnpj}")


def salva_no_banco(nota_fiscal) -> None:
    print(f"Salvando nota fiscal {nota_fiscal.cnpj}")
