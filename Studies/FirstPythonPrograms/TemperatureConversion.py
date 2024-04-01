
try:
    celsius = float(input('Enter the Celsius temperature\n'))
    fahrenheit = float(input('Enter the fahrenheit temperature\n'))


except:
    print('ERRO')




def conversion_celsius(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(f'fahrenheit  :{fahrenheit}')

def conversion_fahrenheit(fahrenheit):
    print(f'celsius :{(fahrenheit - 32) * 5 / 9}')

if __name__ =='__main__':

    conversion_celsius(celsius)
    conversion_fahrenheit(fahrenheit)

