from defenders.top_level_defender import TopLevelDefender
import itertools
import logging
from datetime import datetime


logging.basicConfig(filename='app.log', level=logging.INFO)


class TeamFactory:
    MAX_PLAYERS = 3
    NEW_ID = itertools.count()

    def __init__(self, name, city, country, budget):
        self.id = next(TeamFactory.NEW_ID)
        self.name = name
        self.players = []
        self.assistants = []
        self.managers = []
        self.city = city
        self.country = country
        self.budget = budget
        self.MP = 0
        self.W = 0
        self.D = 0
        self.L = 0
        self.GF = 0
        self.GA = 0
        self.GD = self.GF - self.GA
        self.Pts = 0
        self.YC = 0
        self.RC = 0

    def add_player(self, player):
        if len(self.players) < TeamFactory.MAX_PLAYERS:
            self.players.append(player)
        else:
            logging.error(f"Time of occurrence: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            logging.error("Cannot add more players than the max capacity")

    def get_yellow_cards(self):
        total_count = sum([x.YC for x in self.players])
        return total_count

    def get_red_cards(self):
        total_count = sum([x.RC for x in self.players])
        return total_count

    def get_points(self):
        total_points = self.W * 3 + self.D * 1 + self.L * 0
        return total_points

    def __str__(self):
        return f"{self.id}, {self.name}, {self.city}, {self.country}, {', '.join([x.first_name + ' ' +  x.last_name + ', ' + x.__class__.__name__ for x in self.players])}"
