from MainPlayerConstructor import MainPlayerConstructor


class TopLevelGoalkeeper(MainPlayerConstructor):
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.position = "Goalkeeper"
        self.height = 180
        self.weight = 75

    def get_characteristics(self):
        return {
            "height": self.height,
            "weight": self.weight,
            "appearances": self.appearances
        }

    def __str__(self):
        return f"{self.first_name} {self.last_name} playing as a {self.position}"

