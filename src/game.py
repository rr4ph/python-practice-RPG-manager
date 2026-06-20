from character import Character, load_data
import json, sys
from item import ITEM_DATABASE

class Game:
    def __init__(self):
        self.main_character = None
        self.dummyEasy = Character(100, 100, "Flimsy Dummy", 10)
        self.dummyMedium = Character(150, 150, "Sturdy Dummy", 15)
        self.dummyHard = Character(200, 200, "Invincible Dummy", 20)
        self.dummyCustom = None

    def exit_game(self):
        print("Thanks for playing! Self-annihilation...")
        sys.exit()

    def fight_sequence(self, enemy):
        while self.main_character.health > 0 and enemy.health > 0:
            self.main_character.attack_sequence(enemy)

            if not enemy.health_check():
                break

            enemy.attack_sequence(self.main_character)

            if not self.main_character.health_check():
                break

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

        return Character(max_health, health, name, attack)

    def character_creation_menu(self):
        while True:
            print("""
                1. **Create** character!
                2. **Load** existing character!
                3. **Exit** the game.\n
                """)
            
            
            choice_create = input("Choose your action: \n").lower().strip()

            if choice_create in ["1", "create", "createcharacter"]:
                self.main_character = self.create_character()
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
            Main Menu:
                1. Show Status
                2. Fight Dummy
                3. Save Character
                4. Open Inventory
                5. Exit\n
                """)
            
            choice = input("Choose your action: \n").lower().strip()

            if choice in ["1", "showstatus"]:
                self.main_character.show_character_info()

            elif choice in ["2", "fightdummy"]:
                self.fight_sequence(self.dummyEasy)
                self.main_character.heal_full()
                self.dummyEasy.heal_full()
                print("Character rested up, HP restored to max.")

            elif choice in ["3", "save", "savecharacter"]:
                self.main_character.save_data()
                print(f"{self.main_character.name} has been successfully saved!")
            
            elif choice in ["4", "open", "openinventory"]:
                self.inventory_menu()

            elif choice in ["5", "exit"]:
                self.exit_game()

            else:
                print("Invalid command.")


    def inventory_menu(self):
        while True:
            print("""
            Inventory Menu:
                1. Add item
                2. Remove item
                3. Use item
                4. Check inventory
                5. Exit inventory\n
                """)
            
            choice = input("Choose your action: \n").lower().strip()

            if choice in ["1", "add", "additem"]:
                print("""
                    1. Potion
                    2. Sword
                      """)
                
                item = input("Choose an item to add: \n").lower().strip()
            
                if item in ITEM_DATABASE:
                    self.main_character.inventory.add_inventory_item(
                        ITEM_DATABASE[item]()
                    )
                else:
                    print("This item does not exist.")

            elif choice in ["2", "remove", "removeitem"]:
                if not self.main_character.inventory.items:
                    print("Your inventory is empty.")
                    return
                
                current_items = self.main_character.inventory.open_inventory()
                item = input("Choose an item to remove: \n").lower().strip()
                if item.isdigit():
                    for key, value in current_items.items():
                        if int(key) == int(item):
                            self.main_character.inventory.remove_inventory_item(key)
                            break
                    else:
                        print("There's no item with such ID.")
                        break
                elif item in ITEM_DATABASE:
                    self.main_character.inventory.remove_inventory_item(
                        ITEM_DATABASE[item]()
                    )
                else:
                    print("This item does not exist.")

            elif choice in ["3", "use", "useitem"]:
                if not self.main_character.inventory.items:
                    print("Your inventory is empty.")
                    return
                
                current_items = self.main_character.inventory.open_inventory()
                item = input("Choose the item to use: \n").lower().strip()
                if item.isdigit():
                    for key, value in current_items.items():
                        if int(key) == int(item):
                            self.main_character.inventory.use_inventory_item(key, self.main_character)
                            break
                    else:
                        print("There's no item with such ID.")
                        break
                elif item in ITEM_DATABASE:
                    self.main_character.inventory.use_inventory_item(
                        ITEM_DATABASE[item](),
                        self.main_character
                    )
                else:
                    print("This item does not exist.")
                
            elif choice in ["4", "check", "checkinventory"]:
                self.main_character.inventory.open_inventory()
            
            elif choice in ["5", "exit", "exitinventory"]:
                print("Leaving the inventory...")
                break

            else:
                print("Command is not valid.")