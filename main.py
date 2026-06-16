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

    while True:
        try:
            attack = int(input("Choose the damage of the character(5-20): "))
            if not 5 <= attack <= 20:
                print("Invalid attack value. Try again.")
            else:
                break
        except ValueError:
            print("Invalid value, please, enter whole number.")

    return Character(health, name, attack)

