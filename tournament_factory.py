import pandas as pd


class Tournament:
    def __init__(self, name, country, teams_count):
        self.name = name
        self.country = country
        self.teams_count = teams_count
        self.teams = []
        self.games_played = []

    def get_data_from_game(self, game):
        self.set_host_data(game)
        self.set_away_data(game)

    def set_host_data(self, game):
        host_data = [x for x in self.teams if x.name == game.host]
        host_data[0].GF += game.host_score
        host_data[0].GA += game.away_score
        host_data[0].MP += 1
        points = game.get_points_host()

        if points == 3:
            host_data[0].W += 1
        elif points == 1:
            host_data[0].D += 1
        else:
            host_data[0].L += 1
        host_data[0].YC += game.host_yc
        host_data[0].RC += game.host_rc

    def set_away_data(self, game):
        away_data = [x for x in self.teams if x.name == game.away]
        away_data[0].GF += game.away_score
        away_data[0].GA += game.host_score
        away_data[0].MP += 1
        points = game.get_points_away()

        if points == 3:
            away_data[0].W += 1
        elif points == 1:
            away_data[0].D += 1
        else:
            away_data[0].L += 1
        away_data[0].YC += game.away_yc
        away_data[0].RC += game.away_rc

    def add_team(self, team):
        if len(self.teams) < self.teams_count:
            self.teams.append(team)

    def get_table(self):
        df = pd.DataFrame(columns=["team", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts", "YC", "RC"])
        for team in self.teams:
            df.loc[len(df.index)] = [f"{team.name}", f"{team.MP}", f"{team.W}", f"{team.D}", f"{team.L}", f"{team.GF}", f"{team.GA}", f"{team.GD}", f"{team.get_points()}", f"{team.YC}", f"{team.RC}"]

        return df.sort_values(["Pts", "W", "GF"], ascending=False).set_index(pd.Index([x for x in range(1, 19)]))
