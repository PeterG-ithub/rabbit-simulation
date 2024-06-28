class Chance:
    def __init__(self, name="", data={}) -> None:
        self.name = name
        self.value = data['value']
        self.upper = data['upper']
        self.lower = data['lower']
