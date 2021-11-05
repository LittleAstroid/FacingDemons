class Item(object):

    def __init__(self, type, name, value):
        self.name = name
        self.value = value


class Weapon(Item):

    def __init__(self, name, value, attack_bonus, defence_bonus):
        super(Weapon, self).__init__('wea', name, value)
        self.attack_bonus = attack_bonus
        self.defence_bonus = defence_bonus


class Consumable(Item):

    def __init__(self, name, value, heal, dreadregen):
        super(Consumable, self).__init__('con', name, value)
        self.heal = heal
        self.dreadregen = dreadregen
