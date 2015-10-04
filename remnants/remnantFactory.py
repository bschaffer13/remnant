import random
from abilities.ability import Ability
from attributes import primaryAttributes
import remnants
from remnants import Remnant

MIN_ATTRIBUTES = 20
MAX_ATTRIBUTES = 25
NUM_ABILITIES = 3


class RemnantCreator(object):
    def __init__(self, rid):
        self.remnant = None
        self.rid = rid

    def create_base_remnant(self, name, class_name, min_level, hp_base, speed_base,
                            power_base, evasion_base, spirit_base,
                            crit_chance, species, description, level=None):
        if class_name is None:
            remnant = Remnant.Remnant()
        else:
            remnant = getattr(getattr(remnants, class_name), class_name)

        remnant.name = name
        remnant.remnant_name = name
        if level is None:
            if min_level is not None:
                level = min_level
            else:
                level = 1
        elif level < min_level:
            raise ValueError('Trying to create %s with level %d which is under min level %d' %
                             (name, level, min_level))

        remnant.level = level
        remnant.base_hp = hp_base
        remnant.speed = speed_base
        remnant.power = power_base
        remnant.evasion = evasion_base
        remnant.spirit = spirit_base
        remnant.critical_chance = crit_chance
        if species is not None:
            remnant.species = species
        remnant.description = description
        self.remnant = remnant

    def determine_attributes(self, crit_mult_min, crit_mult_max):
        attribute_points = random.randint(MIN_ATTRIBUTES, MAX_ATTRIBUTES)
        self.remnant.determine_attributes(attribute_points, crit_mult_min, crit_mult_max)

    def level_up(self):
        self.remnant.calculate_level_stats()

    def generate_instance_fields(self):
        remnant = self.remnant

        if remnant.trait is not None:
            trait = remnant.trait.trait_id
        else:
            trait = 0

        return (self.rid, remnant.level, trait, remnant.name, remnant.hp_lvl_mod, remnant.speed_lvl_mod,
                remnant.power_lvl_mod, remnant.evasion, remnant.spirit, remnant.critical_modifier,
                remnant.critical_chance, remnant.base_hp, remnant.speed, remnant.power)

    def generate_trait(self, traits):
        self.remnant.trait = primaryAttributes.random_trait(traits)

    def set_abilities(self, remnant_abilities: list(Ability)):
        remnant = self.rid
        usable_abilities = list(filter(lambda x: x.level <= remnant.level, remnant_abilities))
        for _ in range(min(NUM_ABILITIES, len(usable_abilities))):
            ability = random.choice(usable_abilities)
            usable_abilities.remove(ability)
            remnant.abilities.append(ability)



