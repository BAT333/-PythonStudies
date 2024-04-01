if __name__ ==' __main__':
    pass


Amount = []
try:
    number =int(input('AMOUNT OF NUMBER TO AVERAGE \n'))
    sum = 0
    for _ in range(number):
        Amount.append(int(input('Enter number for average \n')))
    for numbers  in Amount:
        sum = sum+numbers


    print(f'Average was {sum/len(Amount)}')
except:
    print('YOU TYPE SOMETHING WRONG')
