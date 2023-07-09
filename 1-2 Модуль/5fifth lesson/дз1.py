class User:
    def __init__(self, health):
        self.health = health

    def damage(self, damage):
        self.health -= damage

    def attack(self, target):
        damage = 1
        target.take_damage(damage)