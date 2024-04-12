class Livro:
    def __init__(self,título,autor,numero_pagina):
        self._título = título
        self._autor=autor
        self._numero_pagina = numero_pagina
    def __str__(self):
        return f'TITULO {self._título} AUTOR {self._autor} NUMERO DE PAGINA {self._numero_pagina}'