from modelos.enums.sexo import Sexo
from modelos.enums.unidade_federativa import UnidadeFederativa

class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: Sexo, uf: UnidadeFederativa) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.uf = uf

    def __str__(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} \nSexo: {self.sexo.value} \nUf: {self.uf}"