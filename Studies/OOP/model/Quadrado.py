class Quadrado:
    quadrados=[]
    def __init__(self,lado):
        self._lado = lado
        self.quadrados.append(self)
    def __str__(self):
        return f'AREA {self.lado.ljust(10)} , {self.calcular_area()}'
    def mudar_lado(self,lado):
        self._lado = lado

    def calcular_area(self):
        return self._lado*self._lado
    @classmethod
    def lista_quadrados(cls):
        for _ in cls.quadrados:
            print(_)
    @property
    def lado (self):
        return 'GRANDE' if self._lado > 5 else 'PEQUENO'











