import random
from commands import *


class Dragon(Remnant):

    def __init__(self, name='dragon'):
        Remnant.__init__(self, name)
        self.base_hp = 250
        self.hp = self.base_hp
        self.speed = random.randint(60, 70)
        self.power = random.randint(70, 75)
        self.evasion = 5
        self.spirit = 20
        self.critical_modifier = 8
        self.critical_chance = 20
        #self.trait = 'crit'
        self.moves = [DragonBeam(), DragonBreath(), FireBreath()]

    def generate_attribute_point_split(self, attribute_points, num_bins):
        super().generate_attribute_point_split(attribute_points, num_bins)



