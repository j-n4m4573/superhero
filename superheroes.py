import random

class Hero:
    def __init__(self, name, health = 100):
        self.name = name
        self.abilities = list()
        self.amor = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def defend(self):
        for amor in self.amor:
            self.defend()
            self.defense += self.defend()
        if self.health == 0:
            return 0

    def take_damage(self, damage_amount):
        self.health - self.damage_amount
        if self.health == 0:
           self.deaths += 1


    def add_ability(self, ability):
        #Append ability to self.abilities
        self.ability = self.abilities.append(ability)

    def add_kill(self, num_kills):
        self.num_kills = num_kills

    def attack(self):
        attack_counter = 0
        # Call the attack method on every ability in our ability list
        for ability in self.abilities:
            ability.attack()
            attack_counter += ability.attack()
        return attack_counter
        # Add up and return the total of all attacks

class Ability:
    def __init__(self, name, attack_strength):
        #initialize starting values
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
    # Calculate lowest attack value as an integer.
        lowest_attack_value =  self.attack_strength // 2
    # Use random.randint(a, b) to select a random attack value.
        random_attack_value = random.randint(2,7)
    # Return attack value between 0 and the full attack.
        return random.randint(lowest_attack_value, self.attack_strength)

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength

class Weapon(Ability):
    def attack(self):
        return random.randint(0,self.attack_strength)

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def attack(self, other_team):
        total_team_strength = 0
        total_team_kills = 0
        for hero in self.heros:
            total_team_strength += self.heroes.attack_strength
            total_team_kills += self.heroes.num_kills
        self.defend(other_team)

    def defend(self, damage_amount):
        total_defense = 0
        for hero in self.heros:
            total_defense += hero.defense

    def deal_damage(self, damage):
        damage = self.damage_amount // len(self.heroes)

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def find_hero(self, name):
        for index, hero in enumerate(self.heroes):
            if name == hero.name:
                return hero
        return 0

    def remove_hero(self, name):
        for index, hero in enumerate(self.heroes):
            if name == hero.name:
                del self.heroes[index]
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

class Amor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)


# big_strength = Ability("Overwhelming Strength", 30000)
# athena = Hero("Athena")
#     # assert athena.attack() == 0
# athena.add_ability(big_strength)
# attack = athena.attack()
# print(attack)

# >       assert attack <= 30000 and attack >= 15000
#
# if __name__ == "__main__":
#     hero = Hero("Black Panther")
#     print(hero.attack())
#     ability = Ability("Biokinesis", 3000)
#     hero.add_ability(ability)
#     print(hero.attack())
#     new_ability = Ability("Super Human Strength", 800)
#     hero.add_ability(new_ability)
#     print(hero.attack())

    # team = Team("One")
    # print(team.find_hero("Alexa"))
