listas = []
dados = {'name':'RAFAEL','idade':'10'}
dados2 = {'name':'AMANDA','idade':'10'}
dados3 = {'name':'JANINA','idade':'10'}
dados4 = {'name':'ARMENIO','idade':'10'}
listas.append(dados)
listas.append(dados2)
listas.append(dados3)
listas.append(dados4)

for lista in listas:
    nome = lista['name']
    if'RAFAEL'==lista['name']:
        lista['name']='JUCA'
        lista.update({'idade':'19'})

for lista in listas:
    nome = lista['name']
    print(lista)

