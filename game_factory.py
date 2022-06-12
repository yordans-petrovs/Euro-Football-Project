from team_factory import TeamFactory
from tournament_factory import Tournament
import itertools


class Game:
    NEW_ID = itertools.count()

    def __init__(self, tournament, host_name, away_name, host_score, away_score, host_yc, away_yc, host_rc, away_rc):
        self.id = next(Game.NEW_ID)
        self.tournament = tournament
        self.host = host_name
        self.away = away_name
        self.host_score = host_score
        self.away_score = away_score
        self.host_yc = host_yc
        self.away_yc = away_yc
        self.host_rc = host_rc
        self.away_rc = away_rc

    def get_points_host(self):
        if self.host_score > self.away_score:
            return 3
        elif self.host_score == self.away_score:
            return 1
        else:
            return 0

    def get_points_away(self):
        if self.host_score < self.away_score:
            return 3
        elif self.host_score == self.away_score:
            return 1
        else:
            return 0
