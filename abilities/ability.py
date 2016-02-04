
class Ability(object):

    def __init__(self, name, description, power, speed, special_modifier, level=1):
        self.name = name
        self.description = description
        self.power = power
        self.speed = speed
        self.special_modifier = special_modifier
        self.level = level


class AoeAbility(Ability):
    pass
