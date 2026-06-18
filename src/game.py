from character import Character, load_data
import json, sys

class Game:
    def __init__(self):
        self.main_character = None
        self.dummy = Character(100, 100, "Dummy", 10)

    def exit_game(self):
        print("Thanks for playing! Self-annihilation...")
        sys.exit()

    def create_character(self):
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

        self.main_character = Character(max_health, health, name, attack)
        return self.main_character

    def character_creation_menu(self):
        while True:
            print("""
                1. **Create** character!
                2. **Load** existing character!
                3. **Exit** the game.\n
                """)
            
            
            choice_create = input("Choose your action: \n").lower().strip()

            if choice_create in ["1", "create", "createcharacter"]:
                self.create_character()
                print(f"{self.main_character.name} has been successfully created!")
                self.main_character.save_data()
                return self.main_character
            elif choice_create in ["2", "load", "loadcharacter", "loadexistingcharacter"]:
                try:
                    self.main_character = load_data()
                    print(f"{self.main_character.name} has been successfully loaded!")
                    return self.main_character
                except json.JSONDecodeError, FileNotFoundError:
                    print("Save file is empty or corrupted.")
            elif choice_create in ["3", "exit", "exitgame"]:
                self.exit_game()
            else:
                print("Invalid command.")

    def main_game_menu(self):
        while True:
            print("""
                1. Show Status
                2. Fight Dummy
                3. Save Character
                4. Exit
                """)
            
            choice = input("Choose your action: \n").lower().strip()

            if choice in ["1", "showstatus"]:
                self.main_character.show_status()
            elif choice in ["2", "fightdummy"]:
                while self.main_character.health > 0 and self.dummy.health > 0:
                    self.main_character.attack_sequence(self.dummy)

                    if not self.dummy.health_check():
                        break

                    self.dummy.attack_sequence(self.main_character)

                    if not self.main_character.health_check():
                        break
                self.main_character.heal_full()
                self.dummy.heal_full()
                print("Character rested up, HP restored to max.")
            elif choice in ["3", "save", "savecharacter"]:
                self.main_character.save_data()
                print(f"{self.main_character.name} has been successfully saved!")
            elif choice in ["4", "exit"]:
                self.exit_game()
            else:
                print("Invalid command.")