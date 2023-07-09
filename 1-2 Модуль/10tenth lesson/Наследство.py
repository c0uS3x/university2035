class User:
    def __init__(self, damage, health):
        self.damage = damage
        self.health = health

class Magician(User):
    def __init__(self, mana):
        self.mana = mana

class Archer(User):
    def __init__(self, range):
        self.range = range

class Warrior(User):
    def __init__(self, critical_damage):
        self.critical_damage = critical_damage