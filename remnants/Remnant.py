import random
from attributes.attribute import Attribute
from events import DeathEvent


class Remnant(object):

    LVL_ATTRIBUTE_MOD = 0.001
    BASE_LVL_MOD = 1.075
    EVASION_BASE = 0.05
    EVASION_MOD = 0.02
    CRIT_CHANCE_MOD = 0.02
    SPIRIT_MOD = 10

    def __init__(self, name='remnant'):
        self.critical_chance = 10
        self.name = name
        self.remnant_name = 'remnant'
        self.level = 1
        self.hp = 0
        self.base_hp = 0
        self.evasion = 5
        self.power = 0
        self.speed = 0
        self.spirit = 0
        self.critical_modifier = 1
        self.owner = None
        self._trait = None
        self.moves = []
        self.critical_chance_modifiers = list()
        self.power_modifiers = list()
        self.crit_chance_max = 80
        self.species = 'remnant'
        self.hp_lvl_mod = 0
        self.speed_lvl_mod = 0
        self.power_lvl_mod = 0
        self.abilities = list()
        self.description = ""

    @property
    def trait(self):
        return self._trait

    @trait.setter
    def trait(self, value: Attribute):
        if value is not None and not isinstance(value, Attribute):
            raise ValueError('Trait must be an attribute')
        self._trait = value
        self._trait.owner = self

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            raise DeathEvent(self)

    def take_heal(self, heal):
        self.hp += heal
        if self.hp > self.base_hp:
            self.hp = self.base_hp

    def calculate_power(self):
        power = self.power
        for mod in self.power_modifiers:
            power = mod.apply(power)
        return power

    def register_events(self, battle):
        pass
    
    def critical_strike(self, target):
        crit_chance = self.apply_critical_chance_modifiers(self.critical_chance, target)
        if crit_chance > self.crit_chance_max:
            crit_chance = self.crit_chance_max
        if random.randint(1, 100) <= crit_chance:
            return True
        else:
            return False

    def apply_critical_chance_modifiers(self, critical_chance, target):
        for mod in self.critical_chance_modifiers:
            critical_chance = mod.apply(critical_chance, target)
        return critical_chance

    def attack_hit(self):
        if random.randint(1, 100) <= self.evasion:
            return False
        else:
            return True

    def __str__(self):
        return "%s: %d" % (self.name, self.hp)

    def generate_attribute_point_split(self, attribute_points, num_bins):
        bins = [0 for _ in range(num_bins)]
        for i in range(attribute_points):
            bins[random.randint(0, num_bins - 1)] += 1
        return bins

    def determine_attributes(self, attribute_points, crit_mult_min=1, crit_mult_max=1):
        num_attributes = 7
        bins = self.generate_attribute_point_split(attribute_points, num_attributes)

        crit = crit_mult_min + bins[5]
        # Critical hits are capped put extra points into critical chance
        if crit > crit_mult_max:
            bins[6] += (crit - crit_mult_max)
            crit = crit_mult_max

        self.critical_modifier = crit
        self.hp_lvl_mod = Remnant.BASE_LVL_MOD + bins[0] * Remnant.LVL_ATTRIBUTE_MOD
        self.speed_lvl_mod = Remnant.BASE_LVL_MOD + bins[1] * Remnant.LVL_ATTRIBUTE_MOD
        self.power_lvl_mod = Remnant.BASE_LVL_MOD + bins[2] * Remnant.LVL_ATTRIBUTE_MOD
        self.evasion += bins[3] * Remnant.EVASION_MOD
        self.spirit += Remnant.SPIRIT_MOD * bins[4]
        self.critical_chance += Remnant.CRIT_CHANCE_MOD * bins[6]

    def calculate_level_stats(self):
        self.base_hp *= self.hp_lvl_mod**self.level
        self.power *= self.power_lvl_mod**self.level
        self.speed *= self.speed_lvl_mod**self.level














