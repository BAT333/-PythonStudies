try:
    number = int(input('Digite um número: '))

    number_factorial = 1

    for i in range(1, number + 1):
        number_factorial *= i

    print("O fatorial de", number, "é:", number_factorial)

except:
    print('ERRO')


lids = [1,34,64,7,9,3,6,82,3]
lids.sort()
print(lids)

