from unittest import TestCase
from remnants.Remnant import *
from unittest import mock


class TestRemnant(TestCase):

    def setUp(self):
        self.name = 'test remnant'
        self.power = 20
        self.base_hp = 100
        self.evasion = 5

        self.test_remnant = Remnant(self.name)
        self.test_remnant.hp = self.base_hp
        self.test_remnant.base_hp = self.base_hp
        self.test_remnant.power = self.power
        self.test_remnant.evasion = self.evasion

    def test_take_damage(self):
        self.test_remnant.take_damage(50)
        expected_hp = 50
        self.assertEquals(self.test_remnant.hp, expected_hp, 'Hp differs got %d expected %d.' %
                          (self.test_remnant.hp, expected_hp))

    def test_take_heal(self):
        heal_size = 30
        self.test_remnant.hp = heal_size
        self.test_remnant.take_heal(heal_size)
        expected_hp = heal_size * 2
        self.assertEquals(self.test_remnant.hp, expected_hp, 'Hp differs got %d expected %d.' %
                          (self.test_remnant.hp, expected_hp))

    def test_calculate_power(self):
        """
        Should return base power no modifiers have been set
        """
        power = self.test_remnant.calculate_power()
        self.assertEquals(power, self.power, 'Power differs got %d expected %d.' %
                          (self.power, self.power))

    @mock.patch('remnants.Remnant.random.randint')
    def test_critical_strike(self, mock_randint):
        mock_randint.return_value = 50
        critical_hit = self.test_remnant.critical_strike(self.test_remnant)
        self.assertEquals(critical_hit, False, 'Critical strike hit unexpectedly.')

    @mock.patch('remnants.Remnant.random.randint')
    def test_attack_hit(self, mock_randint):
        mock_randint.return_value = 10
        hit_success = self.test_remnant.attack_hit()
        self.assertEquals(hit_success, True, 'Attack missed unexpectedly.')

    @mock.patch('remnants.Remnant.random.randint')
    def test_critical_strike_hit(self, mock_randint):
        mock_randint.return_value = 2
        critical_hit = self.test_remnant.critical_strike(self.test_remnant)
        self.assertEquals(critical_hit, True, 'Critical strike missed unexpectedly.')

    @mock.patch('remnants.Remnant.random.randint')
    def test_attack_miss(self, mock_randint):
        mock_randint.return_value = 2
        hit_success = self.test_remnant.attack_hit()
        self.assertEquals(hit_success, False, 'Attack hit unexpectedly.')

    def test_death_event(self):
        with self.assertRaises(DeathEvent):
            self.test_remnant.take_damage(self.base_hp)

#    def test_register_events(self):
#        self.fail()

#    def test_apply_critical_chance_modifiers(self):
#        self.fail()




