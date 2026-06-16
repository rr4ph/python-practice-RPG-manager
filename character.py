class Character:
    def __init__(self, Health, Name, Attack):
        self.Health = Health
        self.Name = Name
        self.Attack = Attack
    
    def ShowStatus(self):
        print(f"{self.Name} has {self.Health} HP and {self.Attack} ATK.\n")

    def HealthCheck(self):
        self.ShowStatus()
        if (self.Health <= 0):
            print(f"{self.Name} has been defeated.\n")
            quit()

    def TakeDamage(self, Target):
        self.Health = self.Health - Target.Attack
        print(f"{self.Name} took {Target.Attack} damage from {Target.Name}.\n")
        self.HealthCheck()

    def AttackSequence(self, Target):
        print(f"{self.Name} attacks {Target.Name}.\n")
        Target.TakeDamage(self)
