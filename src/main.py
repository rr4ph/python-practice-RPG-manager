from character import Character, load_data
import json

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

print("Welcome to RPG Manager v0.2\n")
dummy = Character(100, 100, "Dummy", 10)
while True:
    print("""
          1. **Create** character!
          --- OR ---
          2. **Load** existing character!\n
          """)
    
    
    choice_create = input("Choose your action: \n").lower().strip()

    if choice_create in ["1", "create", "createcharacter"]:
        main_character = create_character()
        print(f"{main_character.name} has been successfully created!")
        main_character.save_data()
        break
    elif choice_create in ["2", "load", "loadcharacter", "loadexistingcharacter"]:
        try:
            main_character = load_data()
            print(f"{main_character.name} has been successfully loaded!")
            break
        except json.JSONDecodeError:
            print("Save file is empty or corrupted.")
        

while True:
    print("""
          1. Show Status
          2. Fight Dummy
          3. Save Character
          4. Exit
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
    elif choice in ["3", "save", "savecharacter"]:
        main_character.save_data()
        print(f"{main_character.name} has been successfully saved!")
    elif choice in ["4", "exit"]:
        print("Thanks for playing! Self-annihilation...")
        break
    else:
        print("Invalid command.")