from interfaces.testInterface import TestInterface
from interfaces.player import Player


class TestPlayer(Player):

    def __init__(self, remnant1=None, remnant2=None, remnant3=None, name=None):
        comlink = TestInterface()
        super().__init__(comlink, remnant1, remnant2, remnant3, name)
        self.commands = None

    def get_commands(self, commands):
        return self.commands

    def set_commands(self, commands):
        # Allows us to set commands from the test
        self.commands = commands