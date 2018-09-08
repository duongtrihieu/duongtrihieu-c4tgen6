grass_shoes = {
    "NAME": "GRASS SHOE",
    "AGI": 2,
    "LUCK": 1,
    "STR": -1,
}

egg_noddle = {
    "NAME": "EGG NODDLE",
    "HP": 10,
    "STA": -2,
}


# inventory = []
# inventory.append(grass_shoes)
# inventory.append(egg_noddle)

# print(inventory)

# def show(age):
# print("my age:", age)
# huy_age = 17
# quang_anh_age = 29
# show(0)
# show(quang_anh_age)

def show_item(game_item):
    print("*" * 10)

    for key, value in game_item.items():
        print(key, ":", value)

    print("*" * 10)


def combat(attacker, defender):
    print(attacker["NAME"], "is beating", defender["NAME"])
    damage = attacker["ATK"] - defender["DEF"]
    if damage > 0:
        defender["HP"] -= damage
        print(defender["NAME"], "lost", damage, "HP")
    else:
        attacker["HP"] = abs(damage)
        print(attacker["NAME"], "lost", damage, "HP")


player = {
    "NAME": "Player",
    "HP": 200,
    "DEF": 100,
    "ATK": 100,
    "LUCK": 50,
}

orc = {
    "NAME": "Orc",
    "HP": 300,
    "DEF": 50,
    "ATK": 50,
    "LUCK": 20,
}

item = {
    "NAME": "GRASS SHOE",
    "SPD": 2,
    "LUCK": 1,
    "ATK": -1,
}

steal_gaunlet = {
    "NAME": "STEAL GAUNLET",
    "DEF": 50,
    "ATK": 100,
}

bronze_shield = {
    "NAME": "BRONZE SHIELD",
    "DEF": 100,
    "ATK": 20,
    "SPD": -5,
}

golden_stick = {
    "NAME": "GOLDEN STICK",
    "HP": 20,
    "ATK": 100,
}

inventory = [steal_gaunlet, bronze_shield, item, golden_stick]
for item in inventory:
    show_item(item)

combat(player, orc)
# show_item(item)
# show_item(steal_gaunlet)
# show_item(bronze_shield)
# for key,value in bronze_shield.items():
# print(key, ":", value)

while True:
    combat(player, orc)
    if orc["HP"] <= 0 or player["HP"] <= 0:
        break

    combat(orc, player)
    if orc["HP"] <= 0 or player["HP"] <= 0:
        break