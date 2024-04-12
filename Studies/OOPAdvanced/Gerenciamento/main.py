from Studies.OOPAdvanced.Gerenciamento.model.livro import Livro
from Studies.OOPAdvanced.Gerenciamento.model.Biblioteca import Biblioteca
l = Livro("VIAGEM MAGICA1","RAFAEL",347)
l1 = Livro("VIAGEM MAGICA2","RAFAEL",347)
l2 = Livro("VIAGEM MAGICA3","RAFAEL",347)
l3 = Livro("VIAGEM MAGICA4","RAFAEL",347)
l4 = Livro("VIAGEM MAGICA5","RAFAEL",347)
print(l)
b = Biblioteca('GRANDES AVENTURAS')
b.add_livro(l)
b.add_livro(l1)
b.add_livro(l2)
b.add_livro(l3)
while True:
    b.list_livros
    i = int(input('QUAL LIVRO VC DESEJA PEGAR EMPRESTADO'))
    b.empresta_livro(i)
    print('ESSES SÃO LIVROS EMPRESTADOS ')
    b.list_livros_emprestados
    print('OQ VC DESEJA FAZER AGORA\n'
          '1 - PEGAR MAIS LIVRO\n'
          '2- DEVOLVER LIVRO\n'
          '3- LISTA LIVROS DISPONIVEL\n'
          '4- SAIR')
    i2 = int(input())
    match i2:
        case 1:
            b.list_livros
            i = int(input('QUAL LIVRO VC DESEJA PEGAR EMPRESTADO'))
            b.empresta_livro(i)
        case 2:
            b.list_livros_emprestados
            i = int(input('QUAL LIVRO VC DESEJA PEGAR DEVOLVER'))
            b.devolver_livro(i)
        case 3:
            b.list_livros
        case 4:
            break







b.empresta_livro(0)
b.empresta_livro(1)
print('----------------------------------------------')
b.list_livros_emprestados
print('----------------------------------------------')
b.devolver_livro(0)
print('----------------------------------------------')
b.list_livros_emprestados
print('----------------------------------------------')
b.list_livros





if __name__ == '__main__':
    pass