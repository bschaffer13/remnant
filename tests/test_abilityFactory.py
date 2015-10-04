from unittest import TestCase
from abilities.ability import *
from abilities.abilityFactory import *


class TestAbilityFactory(TestCase):

    def setUp(self):
        self.name = 'meowmix'
        self.desc = 'cats love it'
        self.power = 10
        self.speed = 0
        self.special_modifier = 0

    def test_create_ability(self):

        result = build_ability(None, self.name, self.desc, self.power,
                                               self.speed, self.special_modifier)

        self.assertIsInstance(result, Ability)
        self.assertEqual(result.name, self.name)
        self.assertEqual(result.description, self.desc)
        self.assertEqual(result.power, self.power)
        self.assertEqual(result.speed, self.speed)
        self.assertEqual(result.special_modifier, self.special_modifier)

    def test_create_ability_ability(self):
        result = build_ability('Ability', self.name, self.desc, self.power,
                                               self.speed, self.special_modifier)

        self.assertIsInstance(result, Ability)
        self.assertEqual(result.name, self.name)
        self.assertEqual(result.description, self.desc)
        self.assertEqual(result.power, self.power)
        self.assertEqual(result.speed, self.speed)
        self.assertEqual(result.special_modifier, self.special_modifier)

    def test_create_ability_aoeability(self):
        result = build_ability('AoeAbility', self.name, self.desc, self.power,
                                               self.speed, self.special_modifier)

        self.assertIsInstance(result, AoeAbility)
        self.assertEqual(result.name, self.name)
        self.assertEqual(result.description, self.desc)
        self.assertEqual(result.power, self.power)
        self.assertEqual(result.speed, self.speed)
        self.assertEqual(result.special_modifier, self.special_modifier)