import random
from attributes.attribute import Attribute


MENTAL_KEY = 1
PHYSICAL_KEY = 2
ELEMENTAL_KEY = 3
TECHNOLOGICAL_KEY = 4
DEMONIC_KEY = 5
ANGELICAL_KEY = 6


class ElementalFocus(Attribute):
    def __init__(self):
        super().__init__('Elemental Focus', "Doubles critical hit chance")


class Vigilant(Attribute):
    def __init__(self):
        super().__init__("Vigilant", "Attack power increases every turn")
        self.power_inc = 1.04
        self.original_power = 0

    def end_of_turn(self):
        self.owner.power *= self.power_inc

    def pre_battle(self):
        self.original_power = self.owner.power

    def on_death_event(self):
        self.owner.power = self.original_power

    def post_battle(self):
        self.owner.power = self.original_power


class Divine(Attribute):
    def __init__(self):
        super().__init__("Divine", "All healing done and received is doubled")


class Efficient(Attribute):
    def __init__(self):
        super().__init__("Efficient", "Mana cost of all allies abilities is cut in half")


class Precognitive(Attribute):
    def __init__(self):
        super().__init__("Precognitive", "View enemies attacks before choosing yours")


class Indomitable(Attribute):
    def __init__(self):
        super().__init__("Indomitable", "Decrease all damage taken by 10% can't be hit for more than 60% of max health")


def random_trait(possible_traits):
    if isinstance(possible_traits, list):
        trait = random.choice(possible_traits)
    elif isinstance(possible_traits, int):
        trait = possible_traits
    else:
        raise ValueError("Traits must be a list or an int received %s" % str(type(possible_traits)))

    if trait == ELEMENTAL_KEY:
        return ElementalFocus()
    elif trait == TECHNOLOGICAL_KEY:
        return Vigilant()
    elif trait == ANGELICAL_KEY:
        return Divine()
    elif trait == DEMONIC_KEY:
        return Efficient()
    elif trait == PHYSICAL_KEY:
        return Indomitable()
    elif trait == MENTAL_KEY:
        return Precognitive()
    else:
        raise ValueError('%s is not a valid primary trait' % str(trait))
