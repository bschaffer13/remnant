
class Attribute(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self._owner = None

    def pre_battle(self):
        pass

    def post_battle(self):
        pass

    def start_of_turn(self):
        pass

    def end_of_turn(self):
        pass

    def on_death_event(self):
        pass

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

