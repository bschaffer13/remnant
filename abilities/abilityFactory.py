import abilities
from abilities.ability import Ability


def build_ability(ability_class, name, description, power, speed, special_modifier, level=1):
    if ability_class is None:
        return Ability(name, description, power, speed, special_modifier, level)
    else:
        return getattr(abilities.ability, ability_class)(name, description, power, speed, special_modifier, level)

