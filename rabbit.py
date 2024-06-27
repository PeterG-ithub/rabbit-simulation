import json


class Rabbit:
    def __init__(self, data) -> None:
        self.age = data['age']  # Base on days
        self.weight = data['weight']  # Base on grams
        self.calories = data['calories']
        self.energy = data['energy']
        self.state = None
        self.chances = {
            'eating': 0.0  # chances of eating
        }

        self.thresholds = {
            'upper_calories': 500,  # lower threshold for calories
            'lower_calories': 2000  # upper threshold for calories
        }


    def eat(self, calories):  # Spend a little amount of energy to gain calories
        self.calories += calories

    def grow(self):  # Grow base on excess calories when sleeping
        growth_rate = 500  # Calories needed to grow 1 gram
        growth_weight = 1 / growth_rate
        self.weight += growth_weight
        self.calories -= growth_rate

    def sleep(self):  # Increase energy levels of rabbit
        self.convert_calories_to_energy()
        self.grow()

    def convert_calories_to_enery(self, calories):
        conversation_rate = .3
        energy_converted = calories * conversation_rate
        self.calories -= calories
        self.energy += energy_converted

        
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