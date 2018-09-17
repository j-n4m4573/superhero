import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.abilities = list()

    def add_ability(self, ability):
        #Append ability to self.abilities
        self.ability = self.abilities.append(ability)

    def attack(self):
        attack_counter = 0
        # Call the attack method on every ability in our ability list
        for ability in self.abilities:
            ability.attack()
            attack_counter += 1
        return attack_counter
        # Add up and return the total of all attacks

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
        return self.attack_strength - random_attack_value

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength

if __name__ == "__main__":
    hero = Hero("Black Panther")
    print(hero.attack())
    ability = Ability("Biokinesis", 3000)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
