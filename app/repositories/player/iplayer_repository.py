# app/repositories/person/iplayer_repository.py
from abc import ABC, abstractmethod

class IPlayerRepository(ABC):
    @abstractmethod
    def add(self, person):
        pass

    @abstractmethod
    def get_all(self):
        pass