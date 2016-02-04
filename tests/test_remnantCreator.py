from unittest import TestCase, mock
from remnants.remnantFactory import *
from attributes.primaryAttributes import *

class TestRemnantCreator(TestCase):

    def setUp(self):
        self.creator = RemnantCreator(0)
        self.name = 'trogdor'
        self.class_name = None
        self.min_level = 0
        self.hp_base = 100
        self.speed_base = 100
        self.power_base = 10
        self.evasion_base = .05
        self.spirit_base = 20
        self.crit_chance = .2
        self.species = 'Dragon'
        self.description = "The Burninator"

    def test_create_base_remnant(self):
        self.creator.create_base_remnant(self.name, self.class_name, self.min_level, self.hp_base, self.speed_base,
                                         self.power_base, self.evasion_base, self.spirit_base, self.crit_chance,
                                         self.species, self.description)
        remnant_instance = self.creator.remnant
        self.assertIsInstance(remnant_instance, Remnant.Remnant)
        self.assertEqual(remnant_instance.name, self.name)
        self.assertEqual(remnant_instance.level, self.min_level)
        self.assertEqual(remnant_instance.base_hp, self.hp_base)
        self.assertEqual(remnant_instance.speed, self.speed_base)
        self.assertEqual(remnant_instance.power, self.power_base)
        self.assertEqual(remnant_instance.evasion, self.evasion_base)
        self.assertEqual(remnant_instance.spirit, self.spirit_base)
        self.assertEqual(remnant_instance.critical_chance, self.crit_chance)
        self.assertEqual(remnant_instance.species, self.species)
        self.assertEqual(remnant_instance.description, self.description)

    @mock.patch('remnants.Remnant.Remnant.generate_attribute_point_split')
    def test_determine_attributes(self, mock_da):
        self.creator.create_base_remnant(self.name, self.class_name, self.min_level, self.hp_base, self.speed_base,
                                         self.power_base, self.evasion_base, self.spirit_base, self.crit_chance,
                                         self.species, self.description)
        mock_da.return_value = [3 for _ in range(7)]
        self.creator.determine_attributes(1, 7)
        remnant = self.creator.remnant
        self.assertEqual(remnant.critical_modifier, 4)
        self.assertAlmostEqual(remnant.hp_lvl_mod, 1.078)
        self.assertAlmostEqual(remnant.speed_lvl_mod, 1.078)
        self.assertAlmostEqual(remnant.power_lvl_mod, 1.078)
        self.assertEqual(remnant.evasion, 0.11)
        self.assertEqual(remnant.spirit, 50)
        self.assertEqual(remnant.critical_chance, 0.2+0.02*3)

    @mock.patch('remnants.Remnant.Remnant.generate_attribute_point_split')
    def test_level_up(self, mock_da):
        self.creator.create_base_remnant(self.name, self.class_name, 10, self.hp_base, self.speed_base,
                                         self.power_base, self.evasion_base, self.spirit_base, self.crit_chance,
                                         self.species, self.description)
        mock_da.return_value = [3 for _ in range(7)]
        self.creator.determine_attributes(1, 7)
        self.creator.level_up()
        remnant = self.creator.remnant
        self.assertAlmostEqual(remnant.base_hp, self.hp_base*1.078**10)
        self.assertAlmostEqual(remnant.power, self.power_base*1.078**10)
        self.assertAlmostEqual(remnant.speed, self.speed_base*1.078**10)

    def test_generate_trait(self):
        self.creator.create_base_remnant(self.name, self.class_name, 10, self.hp_base, self.speed_base,
                                 self.power_base, self.evasion_base, self.spirit_base, self.crit_chance,
                                 self.species, self.description)
        self.creator.generate_trait(1)
        self.assertIsInstance(self.creator.remnant, Precognitive)
