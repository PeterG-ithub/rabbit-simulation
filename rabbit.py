import json
from util import lerp
from attribute import Attribute
from chance import Chance
import random

class Rabbit:
    def __init__(self, data) -> None:
        self.age = data['age']  # Base on days
        self.weight = data['weight']  # Base on grams
        self.calories = Attribute('calories', data['calories'])
        self.energy = Attribute('energy', data['energy'])
        self.state = None
        # Chances
        self.eating = Chance('eating', data['eating'])
        self.sleeping = Chance('sleeping', data['sleeping'])

    def update(self):
        self.update_chance_eating()

    def update_state(self):
        self.update()
        cumulative_chance = self.eating.value + self.sleeping.value
        number = random.random() * cumulative_chance
        if number < self.eating.value:
            self.state = "eating"
            self.eat(200)
        else:
            self.state = "sleeping"
            self.sleep()

    def update_chance_eating(self):
        a = self.eating.lower
        b = self.eating.upper
        t = (self.calories.value - self.calories.lower) / (
            self.calories.upper - self.calories.lower)
        self.eating.value = lerp(a, b, t)

    def eat(self, calories):  # Spend a little amount of energy to gain calories
        self.calories += calories

    def grow(self):  # Grow base on excess calories when sleeping
        growth_rate = 500  # Calories needed to grow 1 gram
        growth_weight = 1 / growth_rate
        self.weight += growth_weight
        self.calories -= growth_rate

    def sleep(self):  # Increase energy levels of rabbit
        self.convert_calories_to_energy(300)
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
    print(f'Rabbit chance of eating before: {rabbit.eating.value}')
    rabbit.update_chance_eating()
    print(f'Rabbit chance of eating after: {rabbit.eating.value}')


# test_rabbit_creation()
test_update_chances_eating()