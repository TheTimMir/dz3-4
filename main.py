from character import Character, Berserk

player_1 = Character(name='Vasya', damage=2)
print(player_1.stats())
player_2 = Berserk(name='Petya', hp=20, damage=3)
print(player_2.stats())

for i in range(3):
    print(f' - РАУНД {i+1}')
    player_1.attack(player_2)
    player_2.attack(player_1)

    print(player_1.stats())
    print(player_2.stats())
