import random


class Entity:

    def __init__(self, name, health_points, attack, defence, initiative, agility, abilities=None):
        self.name = name
        self.health = health_points
        self.max_health = health_points
        self.attack = attack
        self.defence = defence
        self.initiative = initiative
        self.agility = agility

    def damage(self, opponents_defence, opponents_agility):
        has_hit = False
        is_crit = False

        # Cheque de acerto
        if self.agility - opponents_agility + random.randint(0, 5) > -1:
            has_hit = True
            # Acerto
            if random.random() > 0.95:
                # Crítico. Dano crítico ignora defesa.
                is_crit = True
                damage = round(self.attack * (random.randint(10, 15) / 10))
                if damage < 0:
                    damage = 0
            else:
                damage = round((self.attack - (opponents_defence / 2)) * (random.randint(10, 15) / 10))
                if damage < 0:
                    damage = 0
        else:
            damage = 0

        return damage, has_hit, is_crit


class Player(Entity):

    def __init__(self, name, location, dread, health_points, attack, defence, initiative, agility):
        super(Player, self).__init__(name, health_points, attack, defence, initiative, agility)
        self.dread = dread
        self.equipped = [None, 0, 0]
        self.location = location

    def useitem(self, item_object):
        self.health += item_object.heal
        self.dread += item_object.dreadregen

        if self.health > self.max_health:
            self.health = self.max_health
        if self.dread < 0:
            self.dread = 0

    def unequip(self):
        self.equipped = [None, 0, 0]

    def update(self):
        file = open('gamestate')
        compare = open('item_list.csv')

        saved = file.read().split()

        for line in compare.read():
            if saved[2] == line[0]:
                saved[2] = str([line[0], line[3], line[4]])

        self.name = saved[0]
        self.location = saved[1]
        self.equipped = saved[2]
        self.dread = int(saved[3])
        self.health = int(saved[4])
        self.max_health = int(saved[5])
        self.attack = int(saved[6])
        self.defence = int(saved[7])
        self.initiative = int(saved[8])
        self.agility = int(saved[9])

        file.close()
        compare.close()

    def pushgamestate(self):

        gamestate = [self.name,
                     self.location,
                     self.equipped,
                     self.dread,
                     self.health,
                     self.max_health,
                     self.attack,
                     self.defence,
                     self.initiative,
                     self.agility]

        gamestate = '\n'.join(gamestate)

        file = open('gamestate', 'w')
        file.write(gamestate)
        file.close()
