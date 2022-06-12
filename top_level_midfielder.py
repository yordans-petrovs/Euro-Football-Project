from MainPlayerConstructor import MainPlayerConstructor


class TopLevelMidfielder(MainPlayerConstructor):
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.position = "Midfielder"
        self.height = 170
        self.weight = 80

    def get_characteristics(self):
        return {
            "height": self.height,
            "weight": self.weight,
            "speed": self.speed,
            "tackle": self.tackle,
            "creativity": self.creativity,
            "accuracy": self.accuracy,
            "leadership": self.leadership
        }

    def __str__(self):
        return f"{self.first_name} {self.last_name} playing as a {self.position}"
