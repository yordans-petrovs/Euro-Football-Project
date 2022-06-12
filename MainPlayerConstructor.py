from abc import ABC, abstractmethod
import itertools


class MainPlayerConstructor(ABC):
    NEW_ID = itertools.count()

    def __init__(self):
        self.id = next(MainPlayerConstructor.NEW_ID)
        self.team = ""
        self.appearances = 0
        self.mins = 0
        self.goals_scored = 0
        self.goals_conc = 0
        self.assists = 0
        self.YC = 0
        self.RC = 0
        self.speed = 10
        self.tackle = 10
        self.creativity = 10
        self.accuracy = 10
        self.leadership = 10
        self.penalties = 10
        self.diver = 10

    @staticmethod
    @abstractmethod
    def get_characteristics():
        "A static interface"

    @abstractmethod
    def __str__(self):
        pass
