from Studies.OOP.model.Ball import Ball

b = Ball('VERDE','METAL',2)
b.exchange_color('CIANO')
b2 = Ball('AZUL','METAL',4)
b3 = Ball('AMARELO','METAL',6)
b4 = Ball('VERMELHO','METAL',7)
b5 = Ball('ROXO','METAL',9)

print(Ball.list_ball())
if __name__ == '__main__':
    pass