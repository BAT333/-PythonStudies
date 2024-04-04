class Filho:
    def __init__(self, name, idade):
        self._name = name
        self._idade = idade

    def __str__(self):
        return f'NAME {self._name}'
