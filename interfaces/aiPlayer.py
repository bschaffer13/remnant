from interfaces.cliInterface import CliInterface
from command import Command
from interfaces.player import Player


class AiPlayer(Player):

    def __init__(self, remnant1=None, remnant2=None, remnant3=None, name=None):
        comlink = CliInterface()
        super().__init__(comlink, remnant1, remnant2, remnant3, name)

    def get_commands(self, commands):
        for m in self.remnants:
            c = Command(m, self.enemy_player[0], m.moves[0])
            commands.append(c)