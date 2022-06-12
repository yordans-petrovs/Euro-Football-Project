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


# team_names = [
#     "ACM", "Internazionale", "Juventus", "Roma", "Lazio", "Torino", "Bologna", "Cagliari", "Monza",
#     "Ternana", "Fiorentina", "Crotone", "Napoli", "Cremonese", "Peruggia", "Spezia", "Atalanta", "Como"
# ]
# teams_cities = [
#     "Milan", "Milan", "Torino", "Rome", "Rome", "Torino", "Bologna", "Cagliari", "Monza", "Ternana",
#     "Firenze", "Crotone", "Neapol", "Cremona", "Peruggia", "Spezia", "Bergamo", "Como"
# ]
# teams_budgets = [107, 10, 20, 110, 15, 89, 85, 45, 61, 92, 103, 56, 11, 8, 21, 35, 14, 15]
#
# c = Tournament("Serie A", "Italy", 18)
# country = "Italy"
#
# for i in range(18):
#     t = TeamFactory(team_names[i], teams_cities[i], country, teams_budgets[i])
#     c.add_team(t)
# print(c.get_table())
#
# g = Game(c, "ACM", "Internazionale", 2, 0, 0, 1, 0, 0)
# print(g.tournament.name)
# c.get_data_from_game(g)
# print(c.get_table())
# g = Game(c, "Roma", "Internazionale", 2, 0, 0, 1, 0, 0)
# print(g.tournament.name)
# c.get_data_from_game(g)
# print(c.get_table())
