import os

#AQUI CRIA UMA LIST
#nome_pessoa=[]
#aqui FAZ UMA LISTA COM DIFERENTES ATRIBUTOS
nome_pessoa = [{'nome':'rafael','idade':'18'}]

#AQUI PARA DAR PRINT
def menu():
    print('CADASTRO DE PESSOA\n')
    print('1. CADASTRA')
    print('2. LISTA CADASTRO')
    print('3. APAGAR CADASTRO')
    print('4. SAIR')
# PARA PEGAR INFOS DIGITADO E GUARDA INFOS DIGITADA
# NO PY NÃO PRECISA DEFINIR TIPO DA VARIAVEL
def opcao_invalida():
    print('OPCAO INVALIDA')
    main()
def cadastro():
    print('CADASTRO DE PESSOA \n')
    nomes = input('DIGITE NOME DA PESSOA')
    idade = input('DIGITE IDADE DA PESSOA')
    dados_pessoa= {'nome':nomes,'idade':idade}
    nome_pessoa.append(dados_pessoa)
    print(f'PESSOA CADASTRADA {nome_pessoa}')
    main()
def lista_pessoas():
    print('MOSTRA LISTA DE PESSOAS')
    #FOR MOSTANDO CLIENTS CADASTRADOS
    for mostra_lista in nome_pessoa:
        #aqui so faz mostra nome da pessoa
        nome = mostra_lista['nome']
        print(nome)
    main()
def remover_cadastro(numero):
   del nome_pessoa[numero]

   main()
def alterando_resultado(nome):
    for nome_pessoas in nome_pessoa:
        if nome==nome_pessoas['nome']:
            print('entrou')
            #MANEIRA DE ATUALIZAR INFOS
            nome_pessoas['nome'] = 'JUCA'
            nome_pessoas.update({'idade': '19'})

    main()
def escolhe_opcao():
    try:
        opcao_escolhida = int(input('DIGITE UMA DAS OPÇÃO \n'))
        #opcao_escolhida = int(opcao_escolhida)
        # PARA JUNTAR SO PRECISA ULTILIZAR VIRGULA
        print(f'VOCE ESCOLHEU OPÇÃO{opcao_escolhida} ')
        #NÃO TEM DIFERENÇA ENTRE ASPAS SIMPLES E DUPLA
        #PARA MOSTRA QUE IF FAZ PARTE DAQUELE IF RECOMENDADO DEIXAR 4 ESPAÇOS
        #PARA CRIAS FUNÇÃO DEF UM NOME E PARA ABRIR INVES DAS CHAVES USA SEMPRE :
        def finalizando_cadstro():
            # os.system('cls')
            print('SAINDO')

        if opcao_escolhida==1:
            cadastro()
        elif opcao_escolhida==2:
            lista_pessoas()
        elif opcao_escolhida==3:
            remover_cadastro(1)
        elif opcao_escolhida==4:
            #AQUI PARA CHAMAR FUNÇÃO
            finalizando_cadstro()
        elif opcao_escolhida==5:
            alterando_resultado('RAFAEL')
        else:
            opcao_invalida()
    except:
        opcao_invalida()

    #type mostra tipo da variavel
    #print(type(opcao_escolhida))

def main():
    menu()
    escolhe_opcao()


if __name__ =='__main__':
    main()






#ex com case

numero = 1
match numero:
    case 1:
        print('Adicionar restaurante')
    case 2:
        print('Listar restaurantes')
    case 3:
        print('Ativar restaurante')
    case 4:
        print('Finalizar app')
    case _:
        print('Opção inválida!')
for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
    numero = int(input("Digite um número positivo: "))
    if numero > 0:
        break

print("Você digitou:", numero)

numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)

