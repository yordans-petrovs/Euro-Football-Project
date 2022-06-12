from MainPlayerConstructor import MainPlayerConstructor


class TopLevelDefender(MainPlayerConstructor):
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.position = "Defender"
        self.height = 180
        self.weight = 80

    def get_characteristics(self):
        return f""

    def __str__(self):
        return f"{self.first_name} {self.last_name} playing as a {self.position}"
