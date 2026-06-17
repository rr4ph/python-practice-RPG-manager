from character import Character

def create_character():
    name = input("Choose the name of the character: ")
    while True:
        try:
            health = int(input("Choose the health of the character(50-200): "))
            if not 50 <= health <= 200:
                print("Invalid health value. Try again.")
            else:
                break
        except ValueError:
            print("Invalid value, please, enter a whole number.")
    max_health = health
    
    while True:
        try:
            attack = int(input("Choose the damage of the character(5-20): "))
            if not 5 <= attack <= 20:
                print("Invalid attack value. Try again.")
            else:
                break
        except ValueError:
            print("Invalid value, please, enter whole number.")

    return Character(max_health, health, name, attack)

print("Welcome to RPG Manager v0.1\n")
print("Create your character!\n")
main_character = create_character()
dummy = Character(100, 100, "Dummy", 10)

while True:
    print("""
          1. Show Status
          2. Fight Dummy
          3. Exit
          """)
    
    choice = input("Choose your action: \n").lower().strip()

    if choice in ["1", "showstatus"]:
        main_character.show_status()
    elif choice in ["2", "fightdummy"]:
        while main_character.health > 0 and dummy.health > 0:
            main_character.attack_sequence(dummy)

            if not dummy.health_check():
                break

            dummy.attack_sequence(main_character)

            if not main_character.health_check():
                break
        main_character.heal_full()
        dummy.heal_full()
        print("Character rested up, HP restored to max.")
    elif choice in ["3", "exit"]:
        print("Thanks for playing! Self-annihilation...")
        break
    else:
        print("Invalid command.")
    