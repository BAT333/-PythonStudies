# Class  para cria uma clss
class Client:
    nome = ''
    idade = 0


# Para instanciar
client_1 = Client()
client_1.nome = 'RAFAEL'
client_1.idade = 60

client_2 = Client()
client_2.nome = 'Rian'
client_2.idade = 45

clientes = [client_1, client_2]
# para mostra os metos class ou do metodo que vc quer ver
print(dir(client_1))
# para ver os atributos
print(vars(client_1))

if client_1.idade > 18:
    print('É ADULTO')
else:
    print('NÃO É ADULTO')


# construtor -> basicamente vc cria um metodo com __init__ e nisso cria um construtor
# self -> basicamente diz que cada pessoa tem suas infos tem passa self
# para não confundir que um de um e outro é de outro passa isso
# em palavras leigas igual o this em java, ele diferencia que no  metodo init oq é do metodo e que da class
# ele permite que metodos acesse atributo de outra class
# em palavras leigas __init__ define o construtor da classe
# self ->  pode ser qualquer nome, mas ele faz referencia se pessoa 1 esta chamando ele ou pessoa 2
# refererncia atual da instancia que estamos chamando
# __str__ -> para traformar em String e retorna algo

from Filhos import Filho
class Client_constructor:
    clientehe = []
    def __init__(self, nome, idade):
        self._nome = nome.title()
        #aqui mostra _ que atributo é  protegido
        self._idade = idade
        self._ativo = False
        self._Filhos=[]
        Client_constructor.clientehe.append(self)

    def __str__(self):
        return f'{self._nome.ljust(10)} | {self.idade.ljust(10)} | {self.ativo}'

    @classmethod
    def lista_clientes(cls):
        print(f'{"NAME".ljust(10)} | {"IDADE".ljust(10)} | {"FILHOS".ljust(10)} | {"ATIVO"}')
        for _ in cls.clientehe:
            print(f'{_._nome.ljust(10)} | {_.idade.ljust(10)} | {_.media()} |{_.ativo}')
    @property
    def idade(self):
        return 'ADULTO'if self._idade>18 else 'jovem'.upper()
    @property
    def ativo(self):
        return 'ATIVADO'if self._ativo else 'EXCLUIDO'
    def alterandoEstados(self):
        self._ativo = not self._ativo
    def pegando_filhos(self,name, idade):
        fi = Filho(name,idade)
        self._Filhos.append(fi)
    def media(self):
        if not self._Filhos:
            return 'sem filhos'
        else:
            for fi in self._Filhos:
               return self._Filhos




#property ->MUDAR O ATRIBUTO COMO ELE É LIDO
# metodo tem ter mesmo nome do atriubuto
# metodo tem que ser _ protect para poder ser modificado
#deixa os atributos Protegidos
#title() faz com que a primeira letra de cada paralavra seja maiuscula
#.upper() faz com que todas lestras fica miusculas
#classmethod -> metodo não ta referenciado a nem uma instancia mas simmmmmm a class
# tipo lista restaurante, vc tem colocar isso
#cls -> para mostra que vc não precisa de intancia da class
client_Constru = Client_constructor('rafa', 45)

client_Constru.alterandoEstados()
#client_Constru.pegando_filhos('Renanto',34)
#client_Constru.pegando_filhos('Renanto',34)
#client_Constru.pegando_filhos('Renanto',34)
Client_constructor.lista_clientes()




#print(client_Constru)
#print(vars(client_Constru))


# para importa class
#from model.Client import Client
#se da nome da class nome arquivo e nome da class que se quer pegar
#as para dar nome diferente


