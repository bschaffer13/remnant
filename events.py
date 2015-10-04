
class LossEvent(Exception):
    pass


class DeathEvent(Exception):

    def __init__(self, remnant):
        self.remnant = remnant

    def __str__(self):
        return "%s has died" % self.remnant.name

