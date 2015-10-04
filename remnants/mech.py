import random
from commands import MechStrike
from remnants.Remnant import *


class Mech(Remnant):

    def __init__(self, name='mech'):
        Remnant.__init__(self, name)
        self.hp = 300
        self.speed = random.randint(120, 150)
        self.power = random.randint(60, 65)
        self.evasion = 60
        self.spirit = 10
        self.critical_modifier = 2
        self.critical_chance = 10
        #self.trait = 'attack inc'
        self.moves = [MechStrike()]

    def register_events(self, battle):
        def increase_attack():
            self.power *= 1.05
            print('%s power increased to %f' % (self.name, self.power))
        battle.end_turn_events.append(increase_attack)

