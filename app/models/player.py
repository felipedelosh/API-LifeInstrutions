# app/models/player.py
from app.models.person import Person

class Player(Person):
    def __init__(self, id):
        super().__init__(id)
        self._father = None
        self._mother = None

    @property
    def father(self):
        return self._father

    @father.setter
    def father(self, value):
        self._father = value

    @property
    def mother(self):
        return self._mother

    @mother.setter
    def mother(self, value):
        self._mother = value

    def get_json(self):
        json_data = {**self.__dict__}
        json_data['statistics'] = self.statistics.get_json()
        return json_data

    def __repr__(self):
        attributes = ', '.join(f'{key}={value}' for key, value in self.__dict__.items())
        return f'Player({attributes})'
