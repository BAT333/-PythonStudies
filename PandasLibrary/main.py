import pandas as pd

vendas ={'data':['15/11/2003','23/03/2003'],
        'compradores':['RAFAEL','JOSE'],
        'produto':['casa','carro'],
        'valor':['100','400']
        }
tabela_venda = pd.DataFrame(vendas)

print(tabela_venda)
# importando dados
#tabela_venda = pd.read_excel()
# quantas linhas que vc quer ver
print('head',tabela_venda.head())
print('shape',tabela_venda.shape)
print('describe',tabela_venda.describe())

