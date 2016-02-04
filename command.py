import random


class Command(object):

    def __init__(self, caster, target, func):
        self.caster = caster
        self.target = target
        self.func = func
        self.speed = random.randint(0, 100) + self.caster.speed

    def execute_command(self):
        self.func.execute(self.caster, self.target)

    def __lt__(self, other):
        return self.speed > other.speed

    def __str__(self):
        return 'command = %s %s -> %s' % (self.caster.name, self.func.name, self.target.name)
