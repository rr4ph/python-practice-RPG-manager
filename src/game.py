from character import Character, load_data, load_random_enemy
import json, sys, random
from item import ITEM_DATABASE
from textwrap import dedent

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
            print(dedent("""
                1. **Create** character!
                2. **Load** existing character!
                3. **Exit** the game.\n
                """))
            
            
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
            print(dedent("""
            Main Menu:
                1. Show Status
                2. Enter Town
                3. Save Character
                4. Open Inventory
                5. Exit\n
                """))
            
            choice = input("Choose your action: \n").lower().strip()

            if choice in ["1", "showstatus"]:
                self.main_character.show_character_info()

            elif choice in ["2", "enter", "town", "entertown"]:
                self.town_menu()

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
            print(dedent("""
            Inventory Menu:
                1. Add item
                2. Remove item
                3. Use item
                4. Check inventory
                5. Exit inventory\n
                """))
            
            choice = input("Choose your action: \n").lower().strip()

            if choice in ["1", "add", "additem"]:
                print(dedent("""
                    1. Potion
                    2. Sword
                      """))
                
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

    def town_menu(self):
        while True:
            print(dedent("""
            Town of Gloosgaw Menu:
                1. Inn (Restore HP)
                2. Training Grounds (Fight Dummy)
                3. Forest (Enemy encounters)
                4. Exit (Return to main menu)\n
                """))
            
            choice = input("Make your choice: \n").lower().strip()

            if choice in ["1", "inn", "restore", "hp"]:
                print(f"{self.main_character.name} rested at the Inn. HP fully restored.")
                self.main_character.heal_full()
            elif choice in ["2", "training", "fight", "fightdummy", "trainingrounds"]:
                print(f"Ah, {self.main_character.name}, we already set up a row of new dummies. Pick your target.")
                while True:
                    fightChoice = input(dedent("""
                                    Pick your difficulty:
                                    1. Flimsy Dummy (Easy)
                                    2. Sturdy Dummy (Medium)
                                    3. Invincible Dummy (Hard)
                                    4. Adjustable Dummy (Custom)
                                    5. Exit
                                        """)).lower().strip()
                    if fightChoice in ["1", "flimsy", "flimsydummy", "easy"]:
                        print("This one had a rough day, go easy on the guy...or not.")
                        self.fight_sequence_menu(self.dummyEasy)
                        self.dummyEasy.heal_full()
                    elif fightChoice in ["2", "sturdy", "sturdydummy", "medium"]:
                        print("Classic. Go on, give it your best!")
                        self.fight_sequence_menu(self.dummyMedium)
                        self.dummyMedium.heal_full()
                    elif fightChoice in ["3", "invincible", "invincibledummy", "hard"]:
                        print("This one? Even I barely landed a hit, it's a tough nut to crack.")
                        self.fight_sequence_menu(self.dummyHard)
                        self.dummyHard.heal_full()
                    elif fightChoice in ["4", "adjustable", "adjustabledummy", "custom"]:
                        print("Oh, we didn't finish working on this one yet. It's all yours.")
                        self.dummyCustom = self.create_character()
                        self.fight_sequence_menu(self.dummyCustom)
                        self.dummyCustom.heal_full()
                    elif fightChoice in ["5", "exit", "q"]:
                        print("Come back another time, it's been good seeing you!")
                        break
                    else:
                        print(f"We don't have a dummy like that, {self.main_character.name}.")
            elif choice in ["3", "forest", "enemy", "enemyencounter"]:
                print("You enter forest in pursuit of a challenge.\n")
                enemy = load_random_enemy()
                print(f"A {enemy.name} appeared!\n")
                self.fight_sequence_menu(enemy)
                if self.main_character.health == 0:
                    print("You lost consiousness, and later been found by guards and brought back.")
                else:
                    print("Enemy fell by your hand, you return into the city with more experience.")
            elif choice in ["4", "exit", "q", "return", "mainmenu"]:
                print("Returning to the main menu...")
                break
            else:
                print("Command is not valid.")

    def fight_sequence_menu(self, enemy):
        print(f"You've encountered {enemy.name}!\n")
        while self.main_character.health > 0 and enemy.health > 0:
            while True:
                print("Fight menu:")
                self.main_character.show_HP()
                enemy.show_HP()
                print(dedent("""
                        1. Attack
                        2. Use item
                        3. Flee
                        """))
                choice = input("Choose your action: ").lower().strip()
                if choice in ["1", "attack"]:
                    self.main_character.attack_sequence(enemy)
                    if not enemy.health_check():
                        print(f"You found {enemy.gold} coins.\n")
                        self.main_character.gold += enemy.gold
                        return
                    break
                elif choice in ["2", "use", "useitem"]:
                    if not self.main_character.inventory.items:
                        print("Your inventory is empty.")
                        continue
                    self.main_character.inventory.open_inventory()
                    inventory_choice = input("Choose the item to use, or `quit` to leave inventory: ").lower().strip()
                    if inventory_choice.isdigit():
                        inventory_choice = int(inventory_choice)
                    if self.main_character.inventory.use_inventory_item(inventory_choice, self.main_character):
                        break
                    print("Leaving the inventory.")
                elif choice in ["3", "flee"]:
                    if random.random() < 0.5:
                        print(f"You escaped {enemy.name}!")
                        return
                    else:
                        print("Your attempt was unsuccesseful.\n")
                        break
                else:
                    print("Input is not valid.")

            enemy.attack_sequence(self.main_character)
            if not self.main_character.health_check():
                gold_loss = max(1, self.main_character.gold // 10)
                print(f"You lost {gold_loss} coins!\n")
                self.main_character.gold -= gold_loss
                return
                
