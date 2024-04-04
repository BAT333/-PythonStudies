class TV:
    def __init__(self, canal):
        self._canal = canal
        self._volume = 0

    @property
    def canal(self):
        return 'OUTRO CANAL' if self._canal > 5 else 'CANAL LEGAL'

    def __str__(self):
        return f'CANAL {  self.canal  } VOLUME {self._volume}'

    def dimnuir_volume(self, aumentar):
        num1 = float(aumentar)
        if num1.is_integer():
            self._volume = aumentar
        else:
            print('VOLUME INVALIDO')

    def aumentar_volume(self, aumentar):
        num1 = float(aumentar)
        if num1.is_integer() :
            self._volume = aumentar
        else:
            print('VOLUME INVALIDO')


