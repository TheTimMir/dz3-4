class Character:
    def __init__(self, name='', hp=30, damage=1, armor=0):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def attack(self, target):
        target.take_damage(self.damage)

    def take_damage(self, damage):
        # abs - модуль числа (целая часть)
        self.hp -= abs(damage)

    def stats(self):
        return \
            f' === {self.name} ===\n' \
            f' Здоровье: {self.hp}\n' \
            f' Урон: {self.damage}\n' \
            f' Броня: {self.armor}\n'


class Berserk(Character):
    def __init__(self, name='', hp=30, damage=1, armor=0):
        Character.__init__(self, name, hp, damage, armor)
        self.max_hp = self.hp

    def count_damage(self):
        return self.damage + (self.hp / self.max_hp) * self.damage

    def attack(self, target):
        damage = self.count_damage()
        target.take_damage(damage)
        # print(f'{self.name} атаковал {target.name} и нанёс {damage} урона.')


class Samurai(Character):
    def __init__(self, name='', hp=30, damage=5, armor=0):
        Character.__init__(self, name, hp, damage, armor)
        self.math_multi = 0
        self.multiplier = 0

    def count_damage(self):
        math_multi = 1 + self.multiplier / 10
        if self.multiplier >= 5:
            self.multiplier = 0
        else:
            self.multiplier += 1
        return self.damage * math_multi

    def attack(self, target):
        damage = self.count_damage()
        target.take_damage(damage)
