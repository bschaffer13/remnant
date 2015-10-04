from attributes.attribute import Attribute


class StatusEffect(Attribute):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.caster = None

    def on_receive_heal_event(self):
        pass

    def on_cast_heal_event(self):
        pass

    def on_deal_damage_event(self):
        pass

    def on_take_damage_event(self):
        pass

    def on_use_ability_event(self):
        pass

    def apply(self, caster, target):
        self.owner = target
        self.caster = caster
