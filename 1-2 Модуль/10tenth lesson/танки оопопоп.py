import random

class Tank:
    def __init__(self, model, health, armor, min_damage, max_damage):
        self.model = model
        self.health = health
        self.armor = armor
        self.damage = random.randint(min_damage, max_damage)

    def print_info(self):
        print('\n'f'{self.model} имеет {self.health} здоровья и {self.damage} урона')

    def health_down(self, damage):
        self.health -= damage
        print(f'\n[{self.model}]: Командир, по нашему экипажу {self.model} попали, у нас осталось {self.health} здоровья')

    def shoot(self, enemy):
        if enemy.health <= 0 or self.damage >= enemy.health:
            enemy.health = 0
            print(f'[{self.model}]: {enemy.model} уничтожен!')
        else:
            enemy.health_down(self.damage)
            print(f'[{self.model}]: Точно в цель! Теперь у противника {enemy.model} {enemy.health} здоровья')

class SuperTank(Tank):
      def health_down(self, damage):
          super().health_down(damage//2)


tank1 = Tank('T-34', 200, 100, 50, 100)
tank2 = Tank('Mouse', 150, 80, 10, 80)
stank = SuperTank('t3000', 2000, 500, 500, 1000)

tank1.shoot(stank)
stank.shoot(tank1)
tank1.shoot(tank2)