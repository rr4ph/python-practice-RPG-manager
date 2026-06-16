class Character:
    def __init__(self, Health, Name, Attack):
        self.Health = Health
        self.Name = Name
        self.Attack = Attack
    
    def ShowStatus(self):
        print(f"{self.Name} has {self.Health} HP and {self.Attack} ATK.\n")
