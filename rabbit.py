import json


class Rabbit:
    def __init__(self, data) -> None:
        self.age = data['age']
        self.weight = data['weight']
        self.calories = data['calories']
        self.energy = data['energy']
        self.state = None


with open('rabbit_data.json', 'r') as file:
    data = json.load(file)


def test_rabbit_creation():
    rabbit = Rabbit(data)
    print(f'Rabbit age: {rabbit.age}')
    print(f'Rabbit weight: {rabbit.weight}')
    print(f'Rabbit calories: {rabbit.calories}')
    print(f'Rabbit energy: {rabbit.energy}')
    print(f'Rabbit state: {rabbit.state}')


test_rabbit_creation()