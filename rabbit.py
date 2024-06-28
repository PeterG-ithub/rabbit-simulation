import json
from util import lerp
from attribute import Attribute
from chance import Chance


class Rabbit:
    def __init__(self, data) -> None:
        self.age = data['age']  # Base on days
        self.weight = data['weight']  # Base on grams
        self.calories = Attribute('calories', data['calories'])
        self.energy = Attribute('energy', data['energy'])
        self.state = None
        self.chances = {
            'eating': data['chances']['eating'],  # chances of eating
            'sleeping': data['chances']['sleeping']
        }
        self.chances_thresholds = {
            'lower_chance_eating': data['chances_threshold']['lower_chance_eating'],
            'upper_chance_eating': data['chances_threshold']['upper_chance_eating'],
            'lower_chance_sleeping': data['chances_threshold']['lower_chance_sleeping'],
            'upper_chance_sleeping': data['chances_threshold']['upper_chance_sleeping'],
        }

    def update(self):
        self.update_chance_eating()

    def update_state(self):
        self.update()

    def update_chance_eating(self):
        a = self.chances_thresholds['lower_chance_eating']
        b = self.chances_thresholds['upper_chance_eating']
        t = (self.calories.value - self.calories.lower) / (
            self.calories.upper - self.calories.lower)
        self.chances['eating'] = lerp(a, b, t)

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
    print(f'Rabbit calories: {rabbit.calories.value}')
    print(f'Rabbit energy: {rabbit.energy.value}')
    print(f'Rabbit state: {rabbit.state}')


def test_update_chances_eating():
    rabbit = Rabbit(data)
    rabbit.calories.value = 580
    print(f'Rabbit chance of eating before: {rabbit.chances["eating"]}')
    rabbit.update_chance_eating()
    print(f'Rabbit chance of eating after: {rabbit.chances["eating"]}')


# test_rabbit_creation()
test_update_chances_eating()