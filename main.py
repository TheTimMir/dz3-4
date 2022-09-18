from character import *

player_1 = Character(name='Vasya', damage=2)
print(player_1.stats())
player_2 = Samurai(name='Petya', hp=20, damage=5)
print(player_2.stats())

for i in range(7):
    print(f' - РАУНД {i+1}')
    player_1.attack(player_2)
    player_2.attack(player_1)

    print(player_1.stats())
    print(player_2.stats())
