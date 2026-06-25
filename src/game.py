from character import Character, load_data, load_random_enemy, load_enemy
import json, sys, random
from item import ITEM_DATABASE
from textwrap import dedent

class Game:
    def __init__(self):
        self.main_character = None
        self.dummyEasy = Character(100, 100, "Dupu_>I<aI5_JIb", 10)
        self.dummyMedium = Character(150, 150, "Me7apb", 15)
        self.dummyHard = Character(200, 200, "Mrkgrstraklar", 20)
        self.dummyCustom = None

    def exit_game(self):
        print("Thanks for playing! Self-annihilation...")
        sys.exit()

    def create_character(self):
        name = input("Choose the name of the character: ")
        while True:
            try:
                health = int(input("Choose the health of the character(200-350): "))
                if not 200 <= health <= 350:
                    print("Invalid health value. Try again when you're sober.")
                else:
                    break
            except ValueError:
                print("Invalid value, please, enter a whole number before I bomb Iraq.")
        max_health = health

        while True:
            try:
                attack = int(input("Choose the damage of the character(20-35): "))
                if not 20 <= attack <= 35:
                    print("Invalid attack value. Try again, because I'm using Evo Megaknight.")
                else:
                    break
            except ValueError:
                print("Invalid value, please, enter whole number))))")

        return Character(max_health, health, name, attack)

    def character_creation_menu(self):
        while True:
            print(dedent("""
                1. **Create** character!
                2. **Load** existing character!
                3. **Exit** the game.\n
                """))
            
            
            choice_create = input("Choose your action: ").lower().strip()

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
                print("Invalid is you.")

    def main_game_menu(self):
        while True:
            print(dedent("""
            Main Menu:
                1. Show Status
                2. Enter Town
                3. Save Character
                4. Open Everlast Socks
                5. Exit\n
                """))
            
            choice = input("Choose your action: ").lower().strip()

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
                print("Are you sure you want to leave the game? Don't forget to save the character.")
                choice = input("Y/N: ").lower().strip()
                if choice in ["y", "yes"]:
                    self.exit_game()
                elif choice in ["n", "no"]:
                    continue
                else:
                    print("Command is not valid.")

            else:
                print("Invalid is you.")


    def inventory_menu(self):
        while True:
            print(dedent("""
            Inventory Menu:
                1. Remove item
                2. Use item
                3. Check Everlast Socks
                4. Put sock back on foot\n
                """))
            
            choice = input("Choose your action: ").lower().strip()

            if choice in ["1", "remove", "removeitem"]:
                while True:
                    if not self.main_character.inventory.items:
                        print("Your Everlast Socks are empty.")
                        break
                    
                    current_items = self.main_character.inventory.open_inventory()
                    print("You can also quit with `q` or quit command.\n")
                    item = input("Choose an item to remove, or quit: ").lower().strip()

                    if item in ["q", "quit"]:
                        break
                    if item.isdigit():
                        for key, value in current_items.items():
                            if int(key) == int(item):
                                self.main_character.inventory.remove_inventory_item(key)
                                break
                        else:
                            print("There's no item with such ID.")
                    elif item in ITEM_DATABASE:
                        self.main_character.inventory.remove_inventory_item(
                            ITEM_DATABASE[item]()
                        )
                    else:
                        print("This item does not exist.")

            elif choice in ["2", "use", "useitem"]:
                while True:
                    if not self.main_character.inventory.items:
                        print("Your Everlast Socks are empty.")
                        break
                    
                    current_items = self.main_character.inventory.open_inventory()
                    print("You can also quit with `q` or quit command.\n")
                    item = input("Choose the item to use, or quit: ").lower().strip()

                    if item in ["q", "quit"]:
                        break

                    if item.isdigit():
                        for key, value in current_items.items():
                            if int(key) == int(item):
                                self.main_character.inventory.use_inventory_item(key, self.main_character)
                                break
                        else:
                            print("There's no item with such ID.")
                    elif item in ITEM_DATABASE:
                        self.main_character.inventory.use_inventory_item(
                            ITEM_DATABASE[item](),
                            self.main_character
                        )
                    else:
                        print("This item does not exist.")
                
            elif choice in ["3", "check", "checkeverlastsocks"]:
                self.main_character.inventory.open_inventory()
            
            elif choice in ["4", "put", "puton", "putbackon", "q"]:
                print("Putting Everlast Socks back on...")
                break

            else:
                print("Command is not valid.")

    def town_menu(self):
        while True:
            print(dedent("""
            Yakutiya Menu:
                1. Igloo (Restore HP)
                2. Cages (Practice)
                3. Gulag (Enemy encounters)
                4. ATB (Buy and sell goods)
                5. Exit (Return to main menu)\n
                """))
            
            choice = input("Make your choice: ").lower().strip()

            if choice in ["1", "igloo", "restore", "hp"]:
                print(f"{self.main_character.name} froze ass off at the Igloo. HP fully restored.")
                self.main_character.heal_full()

            elif choice in ["2", "practice", "cages", "fightdummy", "trainingrounds"]:
                print(f"Ah, {self.main_character.name}, we already set up a row of guilty people, Pick your target.")
                while True:
                    fightChoice = input(dedent("""
                                    Pick your difficulty:
                                    1. Dupu_>I<aI5_JIb (Easy)
                                    2. Me7apb (Medium)
                                    3. Mrkgrstraklar (Hard)
                                    4. Adjustable Boxers (Custom)
                                    5. Exit
                                        """)).lower().strip()
                    if fightChoice in ["1", "Dupu_>I<aI5_JIb", "flimsydummy", "easy"]:
                        print("Don't turn your back on this one.")
                        self.fight_sequence_menu(self.dummyEasy, lose_gold_on_death=False)
                        self.dummyEasy.heal_full()
                    elif fightChoice in ["2", "Me7apb", "sturdydummy", "medium"]:
                        print("Classic. Go on, use Tolyan!")
                        self.fight_sequence_menu(self.dummyMedium, lose_gold_on_death=False)
                        self.dummyMedium.heal_full()
                    elif fightChoice in ["3", "Mrkgrstraklar", "invincibledummy", "hard"]:
                        print("This one? Even I barely landed a hit, he's a tough nut to crack.")
                        self.fight_sequence_menu(self.dummyHard, lose_gold_on_death=False)
                        self.dummyHard.heal_full()
                    elif fightChoice in ["4", "adjustable", "adjustableboxers", "custom"]:
                        print("Oh, we didn't finish working on this one yet. It's all yours.")
                        self.dummyCustom = self.create_character()
                        self.fight_sequence_menu(self.dummyCustom, lose_gold_on_death=False)
                        self.dummyCustom.heal_full()
                    elif fightChoice in ["5", "exit", "q"]:
                        print("Come back another time, it's been good seeing you!")
                        break
                    else:
                        print(f"We don't have a prisoner like that, {self.main_character.name}.")

            elif choice in ["3", "gulag", "enemy", "enemyencounter"]:
                print("You enter gulag in pursuit of an ass-whooping.\n")
                while True:
                    print(dedent("""
                                1. Random Encounter
                                2. Boss Rush (FINAL CHALLENGE)
                                3. Exit
                                """))
                    
                    choice = input("Choose your action: ").lower().strip()

                    if choice in ["1", "random", "randomencounter"]:
                        enemy = load_random_enemy()
                        print(f"A {enemy.name} appeared!\n")
                        self.fight_sequence_menu(enemy)
                        if self.main_character.health == 0:
                            print("You lost consiousness, and later been revived by Jett.")
                            break
                        else:
                            print("Enemy fell by your hand, +respect.")

                    elif choice in ["2", "boss", "bossrush"]:
                        enemies = [
                            load_enemy("simon"),
                            load_enemy("jdh"),
                            load_enemy("nate"),
                            load_enemy("mykpodik")
                        ]

                        for index, enemy in enumerate(enemies, start=1):
                            print(f"Battle {index}/{len(enemies)}, {enemy.name} approaches!\n")

                            self.fight_sequence_menu(enemy)

                            if self.main_character.health == 0:
                                print("Come back stronger next time!")
                                return
                            
                            print("You eat salo, 50 HP restored.")
                            self.main_character.heal(50)

                        self.victory_screen()   

                    elif choice in ["3", "exit", "q"]:
                        print("You return to the city...")
                        break
                    else:
                        print("Command is not valid.")

            elif choice in ["4", "shop", "buy", "sell"]:
                self.shop_menu()

            elif choice in ["5", "exit", "q", "return", "mainmenu"]:
                print("Returning to the main menu...")
                break
            else:
                print("Command is not valid.")

    def fight_sequence_menu(self, enemy, lose_gold_on_death=True):
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
                        print(f"You found {enemy.gold} UAH.\n")
                        self.main_character.gold += enemy.gold
                        return
                    break
                elif choice in ["2", "use", "useitem"]:
                    if not self.main_character.inventory.items:
                        print("Your Everlast Socks are empty.")
                        continue
                    self.main_character.inventory.open_inventory()
                    inventory_choice = input("Choose the item to use, or `quit` to leave inventory: ").lower().strip()
                    if inventory_choice.isdigit():
                        inventory_choice = int(inventory_choice)
                    if self.main_character.inventory.use_inventory_item(inventory_choice, self.main_character):
                        break
                    print("Putting Everlast Socks back on.")
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
                if lose_gold_on_death:
                    gold_loss = max(1, self.main_character.gold // 10)
                    print(f"You lost {gold_loss} coins!\n")
                    self.main_character.gold -= gold_loss
                self.main_character.heal_full()
                print("You rest up, and restore your health after brutal ass-whooping.")
                return
            
    def shop_menu(self):
        print(f"Welcome to ATB, {self.main_character.name}. Miroshprotets stole last Guiness bottle, so don't ask me.")
        while True:
            print(dedent("""
                        Shop "ATB" Menu:
                        1. Buy items
                        2. Sell items
                        3. Leave\n
                        """))
            
            choice = input("Choose your action: ").lower().strip()

            if choice in ["1", "buy", "buyitems"]:
                print("Here are the items I'm selling!\n")
                while True:
                    print(dedent(f"""
                        {self.main_character.name}'s money: {self.main_character.gold} UAH

                        1. REVO (20 coins)
                        2. Dragon d1JId0 (40 coins)
                        3. Quit\n
                            """))
                    
                    purchase = input("Choose an item to purchase, or quit: ").lower().strip()

                    if purchase in ["3", "quit"]:
                        break

                    if purchase in ITEM_DATABASE:
                        item = ITEM_DATABASE[purchase]()
                        if self.main_character.gold < item.cost:
                            print(f"{self.main_character.name}, you're a bum.")
                            continue
                        else:
                            if self.main_character.inventory.add_inventory_item(item):
                                self.main_character.gold -= item.cost
                                print("Thanks for the purchase!")
                            else:
                                print("Where do you plan to carry all this stuff? Clean up your socks!")
                                continue
                    else:
                        print("This item does not exist.")

            elif choice in ["2", "sell", "sellitems"]:
                print("Oh, let's see what you're offering!")
                while True:
                    print(dedent(f"""
                                {self.main_character.name}'s money: {self.main_character.gold} UAH

                                Dragon d1JId0: 20 coins each
                                REVO: 10 coins each
                                --- OR ---
                                Q: Quit
                                """))
                    self.main_character.inventory.open_inventory()
                    if not self.main_character.inventory.items:
                        break

                    selling_item = input("Choose an item to sell, or quit: ").lower().strip()


                    if selling_item in ["q", "quit"]:
                        break
                    if selling_item.isdigit():
                        selling_item = int(selling_item)
                        if not (1 <= selling_item <= len(self.main_character.inventory.items)):
                            print("There's no item with such ID.")
                            continue
                        integer_to_item = self.main_character.inventory.items[selling_item-1]
                        
                    elif selling_item in ITEM_DATABASE:
                        selling_item = ITEM_DATABASE[selling_item]()

                    if self.main_character.inventory.remove_inventory_item(selling_item):
                        if isinstance(selling_item, int):
                            selling_item = integer_to_item
                        self.main_character.gold += (selling_item.cost // 2)
                        print(f"{self.main_character.name} sold {selling_item.name} for {selling_item.cost // 2} UAH!")
                    else:
                        print()
            
            elif choice in ["3", "leave", "q"]:
                print("Already leaving? Track down the Miroshprotets for me, will ya?")
                break
            else:
                print("Command is not valid.")

    def victory_screen(self):
        print(f"""
===================================

          VICTORY

===================================

Mykpodik admires your strength and gives you a universal clap, and a gymchik pass.

{self.main_character.name}'s journey has come to an end.

""")
                    