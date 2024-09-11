import os
from modelos.pessoas import Pessoa
from modelos.enums.sexo import Sexo
from modelos.enums.unidade_federativa import UnidadeFederativa

os.system("cls || clear")

aluno = Pessoa("Stive", 18, Sexo.MASCULINO, UnidadeFederativa.AMAZONAS.nome)
print(aluno)