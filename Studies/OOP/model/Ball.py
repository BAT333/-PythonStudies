class Ball:
    balls = []

    def __init__(self, color, material, circumference):
        self._color = color
        self._material = material
        self._circumference = circumference
        self.balls.append(self)

    def __str__(self):
        return f'{self._color.ljust(10)} | {self._material.ljust(10)}| {self._circumference}'

    @classmethod
    def list_ball(cls):
        for b in cls.balls:
            print(b)

    @classmethod
    def list_color(cls):
        for b in cls.balls:
            print(b._color)

    @property
    def circumference(self):
        return 'B' if self._circumference > 1 else 'P'

    def exchange_color(self, color):
        self._color = color
