from game_factory import Game
from goalkeepers.goalkeeper_factory import GoalkeeperFactory
from team_factory import TeamFactory
from tournament_factory import Tournament


# create sample collection of teams with their names, cities and budgets
team_names = [
    "team_A", "team_B", "team_C", "team_D", "team_E", "team_F", "team_G", "team_H", "team_I",
    "team_J", "team_K", "team_L", "team_M", "team_N", "team_O", "team_P", "team_Q", "team_R"
]
teams_cities = [
    "city_A", "city_B", "city_C", "city_D", "city_E", "city_F", "city_G", "city_H", "city_I",
    "city_J", "city_K", "city_L", "city_M", "city_N", "city_O", "city_P", "city_Q", "city_R"
]
teams_budgets = [107, 10, 20, 110, 15, 89, 85, 45, 61, 92, 103, 56, 11, 8, 21, 35, 14, 15]

# create a tournament - set the name and the country, as well as teams in the competition
c = Tournament("New Tournament", "country_I", 18)

# fill in the tournament created with the data
for i in range(18):
    t = TeamFactory(team_names[i], teams_cities[i], "country_I", teams_budgets[i])
    c.add_team(t)


def run_the_tournament():
    g = Game(c, "team_A", "team_B", 2, 0, 0, 1, 0, 0)
    c.get_data_from_game(g)
    g = Game(c, "team_C", "team_B", 2, 3, 0, 1, 1, 0)
    c.get_data_from_game(g)
    c.teams[0].add_player(GoalkeeperFactory().get_goalkeeper("top", "S", "L"))

    return c.get_table(sorting_order="standard")


def get_players_in_a_team(team_name):
    team = [x for x in c.teams if x.name == team_name][0]
    index = c.teams.index(team)
    return c.teams[index].__str__()


if __name__ == '__main__':
    print(run_the_tournament())
    print(get_players_in_a_team("team_A"))
