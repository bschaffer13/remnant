from interfaces.aiPlayer import AiPlayer
from interfaces.cliInterface import CliInterface
from interfaces.cliPlayer import CliPlayer
from remnants.dragon import *
from events import LossEvent
from remnants.ghost import Ghost
from remnants.mech import Mech
from interfaces.player import Player
from remnants.Remnant import *
from interfaces import communicationFacade
from interfaces.communicationFacade import send_message


class Battle(object):

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.player1.enemy_player = self.player2
        self.player2.enemy_player = self.player1
        self.psi_player = self.determine_psi()
        self.begin_turn_events = list()
        self.end_turn_events = list()

        for remnant in self.player1:
            remnant.register_events(self)
        for remnant in self.player2:
            remnant.register_events(self)

    def determine_psi(self):
        player1_psi = any(map(lambda x: x.trait == 'psi', self.player1))
        player2_psi = any(map(lambda x: x.trait == 'psi', self.player2))
        if player1_psi ^ player2_psi:
            return self.player1 if player1_psi else self.player2
        return None

    def turn(self):
        for i, m in enumerate(self.player1.remnants + self.player2.remnants):
            send_message('%d: %s %d' % (i + 1, m.name, m.hp))

        commands = list()

        # if psi psi select
        if self.psi_player:
            self.psi_player.enemy_player.get_commands(commands)
            send_message('PSI: Enemy commands')
            for c in commands:
                send_message(c)
            self.psi_player.get_commands(commands)
        else:
            self.player1.get_commands(commands)
            self.player2.get_commands(commands)

        for event in self.begin_turn_events:
            event()
        self.check_battle_state()
        commands.sort()

        for command in commands:
            if command.caster.hp <= 0:
                continue
            if command.target.hp <= 0:
                command.target = command.target.owner[0]
            try:
                command.execute_command()
            except DeathEvent as de:
                send_message(str(de))
                de.remnant.owner.remove(de.remnant)
            self.check_battle_state()
        for event in self.end_turn_events:
            event()
        self.check_battle_state()

    def battle_loop(self):
        while True:
            self.turn()
            self.check_battle_state()

    def check_battle_state(self):
        if all(map(lambda x: x.hp <= 0, self.player1)):
            raise LossEvent("%s lost" % self.player1.name)
        if all(map(lambda x: x.hp <= 0, self.player2)):
            raise LossEvent("%s lost" % self.player2.name)


if __name__ == '__main__':
    communicationFacade.communicator = CliInterface()
    d1 = Dragon('dragon1')
    d2 = Dragon('dragon2')
    g1 = Ghost('ghost1')
    m1 = Mech('mech1')
    m2 = Mech('mech2')
    m3 = Mech('mech3')
    t1 = CliPlayer(d1, d2, g1, name="player Dragon")
    t2 = AiPlayer(m1, m2, m3, name='player Mech')
    b = Battle(t1, t2)

    try:
        b.battle_loop()
    except LossEvent as e:
        send_message(str(e))


