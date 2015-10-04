from remnants.Remnant import Remnant, DeathEvent


class RemnantCommand(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def execute(self, m1: Remnant, m2: Remnant):
        pass


class DragonBeam(RemnantCommand):

    def __init__(self):
        RemnantCommand.__init__(self, 'Dragon Beam', "Attack with high critical power")

    def execute(self, m1: Remnant, m2: Remnant):
        attack_power = 1
        if not m2.attack_hit():
            print("%s missed %s" % (m1.name, m2.name))
        crit = 1
        if m1.critical_strike(m2):
            crit = m1.critical_modifier

        dmg = (m1.calculate_power() + attack_power) * crit

        print("%s did %d damage to %s" % (m1.name, dmg, m2.name))

        m2.take_damage(dmg)


class FireBreath(RemnantCommand):

    def __init__(self):
        RemnantCommand.__init__(self, 'Fire Breath', "Unavoidable attack that hits all enemies")

    def execute(self, m1: Remnant, m2: Remnant):
        attack_power = m1.calculate_power()/3 + 20
        deaths = list()
        for enemy in m1.owner.enemy_team:
            crit = 1
            if m1.critical_strike(enemy):
                crit = m1.critical_modifier

            dmg = attack_power * crit

            print("%s did %d damage to %s" % (m1.name, dmg, enemy.name))

            try:
                enemy.take_damage(dmg)
            except DeathEvent as de:
                deaths.append(de)
        for de in deaths:
            raise de


class DragonBreath(RemnantCommand):

    def __init__(self):
        RemnantCommand.__init__(self, 'Dragon Breath', "Increase crit chance against target")

    def execute(self, m1: Remnant, m2: Remnant):
        class DoubleCrit(object):
            def __init__(self):
                self.modified_remnant = m2

            def apply(self, crit, target):
                if target == m2:
                    return crit * 2
                else:
                    return crit
        for ally in m1.owner:
            for mod in ally.critical_chance_modifiers:
                if mod.modified_remnant == m2:
                    ally.critical_chance_modifiers.remove(mod)
            ally.critical_chance_modifiers.append(DoubleCrit())


class DarkPact(RemnantCommand):

    def __init__(self):
        RemnantCommand.__init__(self, 'Dark Pact', "Increase power of target for half it's health")

    def execute(self, m1: Remnant, m2: Remnant):
        class _DarkPact(object):
            def __init__(self):
                self.m2 = m2

            def apply(self, power):
                self.m2.power_modifiers.remove(self)
                return power * 4

        if m2 not in m1.owner.mons:
            print('Dark Pact can only be cast on ally')
            return
        print('%s formed a pact with %s' % (m1.name, m2.name))
        m2.power_modifiers.append(_DarkPact())


class DarkTouch(RemnantCommand):

    def __init__(self):
        RemnantCommand.__init__(self, 'Dark Touch', "Strong Attack")

    def execute(self, m1: Remnant, m2: Remnant):
        attack_power = 40
        if not m2.attack_hit():
            print("%s missed %s" % (m1.name, m2.name))
        crit = 1
        if m1.critical_strike(m2):
            crit = m1.critical_modifier

        dmg = (m1.calculate_power() + attack_power) * crit

        print("%s did %d damage to %s" % (m1.name, dmg, m2.name))


class VengeancePact(RemnantCommand):

    def __init__(self):
        RemnantCommand.__init__(self, 'Vengeance Pact', "Restore all health of target but sacrifices caster")

    def execute(self, m1: Remnant, m2: Remnant):

        print('%s formed a pact with %s' % (m1.name, m2.name))
        m2.take_heal(m2.base_hp)

        print('%s rests in piece' % m1.name)
        m1.take_damage(m1.hp)


class MechStrike(RemnantCommand):

    def __init__(self):
        RemnantCommand.__init__(self, 'Mech Strike', "Fast attack")

    def execute(self, m1: Remnant, m2: Remnant):
        attack_power = 20
        if not m2.attack_hit():
            print("%s missed %s" % (m1.name, m2.name))
        crit = 1
        if m1.critical_strike(m2):
            crit = m1.critical_modifier

        dmg = (m1.calculate_power() + attack_power) * crit

        print("%s did %d damage to %s" % (m1.name, dmg, m2.name))

        m2.take_damage(dmg)


