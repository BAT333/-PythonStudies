class Biblioteca:


    def __init__(self, nome):
        self._nome = nome
        self._livros = []
        self._livros_emprestados= []


    @property
    def list_livros(self):
        for i , livros in enumerate(self._livros):
            mensagem= f'{i} NOME DO LIVRO {livros._título}'
            print(mensagem)
    @property
    def list_livros_emprestados(self):
        for i , livros in enumerate(self._livros_emprestados):
            mensagem= f'{i} NOME DO LIVRO {livros._título}'
            print(mensagem)

    def add_livro(self,livro):
        self._livros.append(livro)

    def empresta_livro(self,i):
        livroEmprestado = self._livros.pop(i)
        self._livros_emprestados.append(livroEmprestado);
    def devolver_livro(self,i):
        self._livros.append(self._livros_emprestados[i])
        self._livros_emprestados.pop(i)

