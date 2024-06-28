class Attribute:
    def __init__(self, name="", data={}) -> None:
        self.name = name 
        self.value = data['value'] or 0
        self.upper = data['upper'] or 0
        self.lower = data['lower'] or 0
