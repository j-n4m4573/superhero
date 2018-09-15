import random





class Ability:
    def __init__(self, name, attack_strength):
        #initialize starting values
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
    # Calculate lowest attack value as an integer.
        lowest_attack_value = 0
    # Use random.randint(a, b) to select a random attack value.
        random_attack_value = random.randint(2,7)
    # Return attack value between 0 and the full attack.
        return random_attack_value
    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength

class Hero:
    def __init__(self, name):
        self.name = name
        self.abilities = list()

    def addAbility(self, ability):
        #Append ability to self.abilities
