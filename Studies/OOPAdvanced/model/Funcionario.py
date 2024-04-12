from Studies.OOPAdvanced.model.Pessoa import Pessoas


class Funcionario(Pessoas):
    def __init__(self, nome, idade, cargo=' DESEMPREGADO'):
        super().__init__(nome, idade)
        self._cargo = cargo
        self._contas = []

    def __str__(self):
        return f'NOME: {self._nome} IDADE: {self.adulto_jovem} CARGO:{self._cargo}'

    def adicionar_conta(self, conta):
        self._contas.append(conta)
    @property
    def lista_contas(self):
        for i,conta in enumerate(self._contas):
            mensagem = f'{i}- NUMERO DA CONTA {conta._numero_conta} SALDO DA CONTA {conta._saldo}'
            print(mensagem)



