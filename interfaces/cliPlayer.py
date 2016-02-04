from interfaces.cliInterface import CliInterface
from command import Command
from interfaces.player import Player


class CliPlayer(Player):

    def __init__(self, remnant1=None, remnant2=None, remnant3=None, name=None):
        comlink = CliInterface()
        super().__init__(comlink, remnant1, remnant2, remnant3, name)

    def get_commands(self, commands):

        self.comlink.send_message('Player 1 choose commands')
        for i, m in enumerate(self.remnants):
            self.comlink.send_message('%d: %s' % (i + 1, m))

        while True:
            cmd = self.comlink.get_input('command')
            if not len(cmd):
                break
            self.comlink.send_message(cmd)
            try:
                caster, move = map(lambda x: int(x) - 1, cmd.split())
            except ValueError:
                self.comlink.send_message('Input must be two ints')
                continue

            if caster < 0 or caster > 2 or caster > len(self.remnants):
                self.comlink.send_message('Invalid caster selected')
                continue

            if move < 0 or move > 2 or move >= len(self.remnants[caster].moves):
                self.comlink.send_message('Invalid move selected')
                continue

            self.comlink.send_message('Targets')
            for i, m in enumerate(self.enemy_player.remnants + self.remnants):
                self.comlink.send_message('%d: %s %d' % (i + 1, m.name, m.hp))

            target = self.comlink.get_input('Choose Target')

            try:
                target = int(target) - 1
            except ValueError:
                self.comlink.send_message('Target must be a number')
                continue

            if target < 0 or target > 5:
                self.comlink.send_message('Invalid target selected')
                continue

            if target >= len(self.enemy_player):
                t = self.remnants[target - len(self.enemy_player)]
            else:
                t = self.enemy_player[target]

            for command in commands:
                if command.caster == self.remnants[caster]:
                    self.comlink.send_message('Overwriting old command for %s' % self.remnants[caster].name)
                    commands.remove(command)
            c = Command(self.remnants[caster], t, self.remnants[caster].moves[move])
            commands.append(c)

