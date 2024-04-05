class Conta:
    def __init__(self, numero_conta, nome, saldo=0):
        self._numero_conta = numero_conta
        self._nome = nome
        self._saldo = saldo

    def __str__(self):
        return f'NOME {self._nome}  NUMERO DA CONTA {self._numero_conta} SALDO {self._saldo}'

    def altera_nome(self, nome):
        self._nome = nome

    def depositar_salfo(self, saldo):
        if saldo > 0:
            self._saldo = saldo
        else:
            print('SALDO INVALIDO')

    def sacar_saldo(self, saldo):
        if saldo < self._saldo:
            self._saldo = self._saldo - saldo
        else:
            print('INVALIDO')
