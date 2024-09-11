from enum import Enum

class UnidadeFederativa(Enum):
    BAHIA = "Bahia", "Ba"
    SAO_PAULO = "São Paulo", "SP"
    AMAZONAS = "Amazonia","AM"

    def __init__(self, nome: str, sigla: str) -> None:
        self.nome = nome
        self.sigla = sigla
