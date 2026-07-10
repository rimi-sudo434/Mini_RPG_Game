import random
import time

# Player setup
player_name = input("Enter your hero name: ")

player_hp = 100
player_max_hp = 100
player_level = 1
player_xp = 0

# Enemy setup
enemy_name = "Dragon"
enemy_hp = 100

print("\n🔥 Welcome,", player_name)
print("⚔️ A wild", enemy_name, "appeared!")

time.sleep(1)

# Battle loop
while player_hp > 0 and enemy_hp > 0:

    print("\n---------------------")
    print(player_name, "HP:", player_hp, "/", player_max_hp)
    print(enemy_name, "HP:", enemy_hp)
    print("---------------------")

    print("1. ⚔️ Attack")
    print("2. 💚 Heal")
    print("3. 🔥 Special Attack")

    choice = input("Choose your action: ")

    # Player attack
    if choice == "1":
        damage = random.randint(10, 25)
        enemy_hp -= damage
        print("\n⚔️ You attacked the Dragon!")
        print("You dealt", damage, "damage.")

    # Healing
    elif choice == "2":
        heal = random.randint(10, 20)
        player_hp += heal

        if player_hp > player_max_hp:
            player_hp = player_max_hp

        print("\n💚 You healed yourself by", heal, "HP.")

    # Special attack
    elif choice == "3":
        damage = random.randint(20, 40)
        enemy_hp -= damage
        print("\n🔥 SPECIAL ATTACK!")
        print("You dealt", damage, "damage.")

    else:
        print("\n❌ Invalid choice!")
        continue

    # Enemy turn
    if enemy_hp > 0:
        enemy_damage = random.randint(5, 20)
        player_hp -= enemy_damage

        print("\n🐉 Dragon attacks!")
        print("Dragon dealt", enemy_damage, "damage.")

    time.sleep(1)


# Game result
print("\n====================")

if player_hp > 0:
    print("🎉 YOU WON!")
    print("You defeated the Dragon!")
    player_xp += 100
    print("XP gained:", player_xp)

else:
    print("💀 YOU LOST!")
    print("The Dragon defeated you.")

print("====================")
print("Game Over!")