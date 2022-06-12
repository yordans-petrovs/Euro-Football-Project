from MainPlayerConstructor import MainPlayerConstructor


class TopLevelForward(MainPlayerConstructor):
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.position = "Forward"
        self.height = 170
        self.weight = 80
        self.speed = 10

    def get_characteristics(self):
        return {
            "height": self.height,
            "weight": self.weight,
        }

    def __str__(self):
        return f"{self.first_name} {self.last_name} playing as a {self.position}"

