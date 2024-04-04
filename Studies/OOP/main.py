from Studies.OOP.model.Ball import Ball
from Studies.OOP.model.Quadrado import Quadrado
from Studies.OOP.model.Pessoa import Pessoas
from Studies.OOP.model.TV import TV
q = Quadrado(5)
q1 = Quadrado(7)
q3 = Quadrado(9.4)
q2 = Quadrado(7)
q3 = Quadrado(0.34)

q.lista_quadrados()


b = Ball('VERDE','METAL',2)
b.exchange_color('CIANO')
b2 = Ball('AZUL','METAL',4)
b3 = Ball('AMARELO','METAL',6)
b4 = Ball('VERMELHO','METAL',7)
b5 = Ball('ROXO','METAL',9)
print(Ball.list_ball())

print('-------------------------------------------')
p = Pessoas('RAFAEL',19,60,1.75)
for _ in range(4):
    p.Envelhercer()
p1 = Pessoas('JANAINA',50,60,1.75)
p2 = Pessoas('ARMENIO',49,60,1.75)
p3 = Pessoas('RIAN',15,60,1.75)
p4 = Pessoas('RENAN',10,60,1.75)
Pessoas.list_pessoas()
print('-------------------------------------------')
tv = TV(5)
tv.dimnuir_volume(103)
print(tv)
if __name__ == '__main__':
    pass