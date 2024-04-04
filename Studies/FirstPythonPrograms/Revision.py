# COMO DAR PRINT
print('OLA MUNDO ')
#input para pegar resultado de terminal
numero  =int(input('NUMERO ESCOLHIDO \n'))
#if else
# if 25 <= tempo <= 45:
# usar and ou or
if numero == 5:
    print(f' NUMERO ESCOLHIDO {numero}')
elif numero == 2:
    print(f'NUMERO ESCOLHIDO FOI {numero}')
else:
    print('VC NÃO ESCOLHEU UM NUMERO BOM')



#PARA CRIA UM FUNÇÃO SO COLOCA DEF E NOME E ABRIR PARENTES
#def mostra_numero(numero):
def mostra_numero(numero):
    if numero == 5:
        print(f' NUMERO ESCOLHIDO {numero}')
    elif numero == 2:
        print(f'NUMERO ESCOLHIDO FOI {numero}')
    else:
        print('VC NÃO ESCOLHEU UM NUMERO BOM')



#Try except tratamento de erro

try:
    numero_reserva = int(input('NUMERO ESCOLHIDO \n'))
except:
    print('OPÇÃO INVALIDA ')

#LISTA
# PARA CRIA UMA LISA VAZIA BASTA DAR NOME PARA ELA ABRIR CONCHESTES
#ex ;  nome = []

nomes = []
# fazendo for para add nome nessa lista 5 vezes
for _ in range(1):
    valores = input('NOMES \n')
    nomes.append(valores)
    print(f'NOME {nomes}')


#PARA ATUALIZAR VALORES
for i, nome in enumerate(nomes):
    if 'R' == nome:
        print('entrou')
        nomes[i] = 'RAFAEL'

print(nomes)
#FAZENDO FOR PARA EXIBIR TODOS NOMES
for nome in nomes:
    if 'R' == nome:
        print('entrou')
        # REMOVENDO
        nomes.remove(nome)


for nome in nomes:
    print(nome)

#for _ in range(5):
#FOR SE DA VALOR PARA ELE COM RANGE PEDE PARA ELE REPETIR QUANTAS VEZES VC QUISER
#for nome in nomes: -> da primeiro nome depois o  da lista que vc quer passar

#while
#while condição:
    # Bloco de código a ser repetido



numero_A = -1
while numero_A <= 0:
    numero_A = int(input("Digite um número positivo: "))

print("Você digitou:", numero_A)

# isso mostra que arquivo é principal isso não pode ser importado nem nada do tipo



#FAZENDO UMA LISTA MAIS COMPLEXA, ATUALIZANDO E REMOVENDO VALORES DELA
#COM DICIONARIO DENTRO
#PRIMEIRO CRIA UMA LISTA SIMPLES
dados_pessoas = []
for _ in range(1):
    nome = input('DIGITA UM NOME')
    idade = int(input('DIGITA A IDADE'))
#DEPOIS MODELA ELA COMO VC QUER SEJA SALVA DENTRO DA LIST
    dados= {'name':nome,'idade':idade}
#DEPOIS SALVA
    dados_pessoas.append(dados)
    print(dados_pessoas)
for dados in dados_pessoas:
    #PARA VC VISUALIZAR DADOS ESPECIFICOS
    #TEM FAZER FOR PEGA OQ VC QUER MOSTRA PARA FOR COMO VC QUER VER
    nome = dados['name']
    print(nome)
for dados in dados_pessoas:
    if dados['name'] == 'RAFAEL':
        #AQUI PARA FAZER UPDATE
        dados['name'] = 'RIAN'
        #outra forma
        dados.update({'idade':'19'})
        print('ENCONTRADO')
print(dados_pessoas)
print("Nome:", dados_pessoas[0]['name'])

if __name__ =='__main__':
    mostra_numero(numero)
    mostra_numero(numero)
    mostra_numero(numero)


credenciais_clientes = {
    'alice123': {'username': 'alice123', 'password': 'alic3P@ssw0rd', 'status': 'active'},
    'bob456': {'username': 'bob456', 'password': 'b0bP@ssword!', 'status': 'inactive'},
    'charlie789': {'username': 'charlie789', 'password': 'Ch@rlieP@ss9', 'status': 'active'}
}
#mostra todos clientes
print(credenciais_clientes)
#mostra um especifico
print(credenciais_clientes['alice123'])
#mostra mais especifico ainda
print(credenciais_clientes['alice123']['username'])


class Funcionario:
    """
    Classe que representa um funcionário da empresa

    Atributos:
        nome (str): O nome do funcionário
        idade (int): A idade do funcionário
        cargo (str): O cargo que o funcionário ocupa na empresa
    """

    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def realizar_tarefa(self, tarefa):
        """
        Simula o funcionário realizando uma tarefa

        Argumentos:
            tarefa (str): A tarefa a ser realizada pelo funcionário

        Retorna:
            str: Uma mensagem indicando que a tarefa foi realizada
        """
        return f"{self.nome} realizou a tarefa: {tarefa}"

#O método __init__ é um método especial em Python que é chamado quando uma instância da classe é criada. Ele é usado para inicializar os atributos da classe com os valores fornecidos. No exercício que passei, o método __init__ é responsável por inicializar os atributos nome, idade e cargo da classe Funcionario com os valores fornecidos quando uma instância de Funcionario é criada. Este método é fundamental para a criação de objetos da classe e a definição de seus atributos iniciais.
#Em Python, self é uma convenção que representa a própria instância da classe. Quando você chama um método em uma instância de classe, o Python automaticamente passa a instância como o primeiro argumento para o método. Por convenção, esse primeiro argumento é chamado de self, mas você pode nomeá-lo de qualquer forma, embora seja altamente recomendado usar self para manter o código claro e legível. O uso de self permite que os métodos acessem e modifiquem os atributos da instância.