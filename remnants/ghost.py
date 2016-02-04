import random
from commands import *


class Ghost(Remnant):

    def __init__(self, name='ghost'):
        Remnant.__init__(self, name)
        self.base_hp = 350
        self.hp = self.base_hp
        self.speed = random.randint(50, 70)
        self.power = random.randint(100, 120)
        self.evasion = 30
        self.spirit = 40
        self.critical_modifier = 3
        self.critical_chance = 10
        #self.trait = 'psi'
        self.moves = [DarkPact(), DarkTouch(), VengeancePact()]





