class Pessoas:
    pessoas = []

    def __init__(self, nome, idade, peso, altura):
        self._nome = nome.title()
        self._idade = idade
        self._peso = peso
        self._altura = altura
        self.pessoas.append(self)

    def __str__(self):
        return f'NOME: {self._nome} IDADE: {self._idade} PESO: {self._peso} ALTURA: {self._altura} IMC: {round(self.imv(),2)}'

    @classmethod
    def list_pessoas(cls):
        for p in cls.pessoas:
            print(p)

    def Envelhercer(self):
        self._idade += 1
        if self._idade < 21:
            self._altura += 0.05
    def engordar(self,peso_ganhado):
        self._peso = self._peso + peso_ganhado

    def emagrecer(self,peso_perdido):
        self._peso = self._peso - peso_perdido

    def cresce(self,altura):
        self._altura = self._altura + altura

    def imv(self):
        return self._peso/(self._altura*self._altura)





