from enum import property

class Pessoas:
    pessoas = []

    def __init__(self, nome, idade):
        self._nome = nome.title()
        self._idade = idade
        self.pessoas.append(self)

    def __str__(self):
        return f'NOME: {self._nome} IDADE: {self.adulto_jovem}'

    @classmethod
    def list_pessoas(cls):
        for p in cls.pessoas:
            print(p)

    @property
    def adulto_jovem(self):
        return 'ADULTO' if self._idade >= 18 else 'JOVEM'

#CRIAR UMA CLASS ABSTRACT
#from abc import ABC, abstractmethod
#    def __init__(self, nome, idade,ABC):
#  @abstractmethod
 #   def a  (self):

