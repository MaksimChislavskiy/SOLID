from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print('Удар мечем')

    def __str__(self):
        return 'Меч'


class Bow(Weapon):
    def attack(self):
        print('Выстрел из лука')

    def __str__(self):
        return 'Лук'

class Fighter():
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f'Боец {self.name} выбрал {self.weapon}')


class Monster():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

def fight(fighter: Fighter, monster: Monster):
    fighter.weapon.attack()
    print(f'Монстр {monster} побежден!')

sword = Sword()
bow = Bow()
monster = Monster('Гоблин')
ivan = Fighter('Иван')
ivan.change_weapon(sword)
ivan.change_weapon(bow)
fight(ivan, monster)