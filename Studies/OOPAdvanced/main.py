from Studies.OOPAdvanced.model.Funcionario import Funcionario
from Studies.OOPAdvanced.model.Conta import Conta
c = Conta('34234234234324','RAFAEL')
p = Funcionario('RAFAEL',18,'ENGENHEIRO DE SOFTWARE')
p.adicionar_conta(c)
p.adicionar_conta(c)
p.adicionar_conta(c)
print(p)
print('----------------------------------------------')
p.lista_contas
if __name__=='__main__':
    pass