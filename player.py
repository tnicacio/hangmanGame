class Player:

    def __init__(self, name, health: int = 6):
        self._name = name
        self._health = health
        self._won = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health: int):
        if health < 0:
            raise ValueError('Player health cannot be negative')
        self._health = health

    @property
    def won(self):
        return self._won

    @won.setter
    def won(self, value: bool):
        self._won = value

    def __str__(self):
        return f'Player: {self.name} - HP: {self._health}'
