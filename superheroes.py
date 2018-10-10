import random




class Hero:
    def __init__(self, name, health = 100):
        self.name = name
        self.abilities = list()
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def defend(self):
        total_defense = 0
        for armor in self.armors:
            armor.defend()
            total_defense += armor.defend()
        if self.health == 0:
            return 0
        else:
            return total_defense

    def take_damage(self, damage_amount):
        self.health -=  damage_amount
        if self.health <= 0:
           self.deaths += 1

    def add_ability(self, ability):
        #Append ability to self.abilities
        self.ability = self.abilities.append(ability)

    def add_kill(self, num_kills):
        self.kills = num_kills

    def add_armor(self, armor):
        self.armor = self.armors.append(armor)

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
        self.number_of_kills = 0

    def attack(self, other_team):
        # attack other team
        total_team_strength = 0
        for hero in self.heroes:
        # add each heros attack power to total strength of the teams attack
            total_team_strength += hero.attack()
        # call the defend method on the other team
        self.number_of_kills = other_team.defend(total_team_strength)
        # number of kills per hero
        kills_per_hero = self.number_of_kills // len(self.heroes)
        # add kills per hero to each hero
        for hero in self.heroes:
            hero.add_kill(kills_per_hero)

    def defend(self, damage_amount):
        total_defense = 0
        # total defense from each hero
        for hero in self.heroes:
            total_defense += hero.defend()
        # damage left after defense
        total_damange_after_defense = damage_amount - total_defense
        # if damage after defense if greater than zero
        # attack has to be greater than the defense to do damage
        if total_damange_after_defense > 0:
            number_of_deaths = self.deal_damage(total_damange_after_defense)
            return number_of_deaths
        else:
            return 0

    def deal_damage(self, damage):
        number_of_deaths = 0
        # divide damage amongst heros
        damage_per_hero = damage // len(self.heroes)
        # deal damage to each hero
        for hero in self.heroes:
            hero.take_damage(damage_per_hero)
        # if the heros healh after damage is less than or equal to 1, the team
        # takes a loss
            if hero.health <= 0:
                number_of_deaths += 1
        return number_of_deaths

    def revive_heroes(self, health = None):
        for hero in self.heroes:
        #if a value is not given for hero health, then assign starting health
        # to the hero
            if health is None:
                hero.health = hero.start_health
            else:
                hero.health = health

    def stats(self):
        for hero in self.heroes:
            print("{} D: {} K: {}".format(hero.name, hero.deaths, hero.kills))
    def update_kills(self):
        for hero in self.heroes:
            print(self.heroes.num_kills)

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

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)

class Arena:
    def __init__(self):
        self.team_one = Team("team_one")
        self.team_two = Team("team_two")
        # team_one_name = input("Player one: Please choose a name")
        # self.team_one = Team(team_one_name)
        self.build_team_one(self.team_one)
        #
        # team_two_name = input("Player two: Please choose a name")
        # self.team_two = Team(team_two_name)
        self.build_team_two(self.team_two)
        self.team_battle()
        self.show_stats()

    def build_team_one(self, name):
        # builds team one
        # team_one_name = input("Player one: Please choose a name")
        # self.team_one = Team("team_one")

        for i in range(0,num):
            self.team_one.heroes.append(Hero(new_heroes[i]))

        for hero in self.team_one.heroes:
            new_armor = Armor(armors[random.randint(0,4)], armor_power)
            hero.add_armor(new_armor)
            new_ability = Ability(abilities[random.randint(0,4)], ability_power)
            hero.add_ability(new_ability)

    def build_team_two(self, name):
        # builds team two
        # team_two_name = input("Player two: Please choose a name")
        # self.team.two = Team(team_two_name)

        for i in range(0,num):
            self.team_two.heroes.append(Hero(new_heroes[i]))

        for hero in self.team_two.heroes:
            new_armor = Armor(armors[random.randint(0,4)], armor_power)
            hero.add_armor(new_armor)
            new_ability = Ability(abilities[random.randint(0,4)], ability_power)
            hero.add_ability(new_ability)


    def team_battle(self):
        # method to continue battle until one team is dead
        teams = [self.team_one, self.team_two]
        # choose attack team
        attack_team = teams[random.randint(0,1)]
        if attack_team == self.team_one:
            defend_team = self.team_two
        else:
            defend_team = self.team_one

        while attack_team.number_of_kills <= 4 or defend_team.number_of_kills <= 4:
            attack_team.attack(defend_team)
            defend_team.attack(attack_team)

    def show_stats(self):
        self.team_one.stats()
        self.team_two.stats()

new_heroes = ["Tom", "Jake", "Mike", "Chris", "Ralph", "Morty", "Koji", "Jarro", "Karmicheal", "Kingston"]
armors = ["hat", "socks", "shoes", "shirt", "spatula", "cape", "du-rag", "stocking cap", "beanie", "sweater vest", "toupe"]
abilities = ["mind control", "aura vision", "teleportation", "telescopic vision","superhuman strength", "telekinesis", "Magma Manipulation", "Electromagnetic Manipulation"]
armor_power = random.randint(0, 300)
ability_power = random.randint(0, 400)
team_one = list()
team_two = list()
num = 4

new_arena = Arena()
new_arena.team_battle()

champions = Team("champions")
the_winners = Team("the winners")

for i in range(0,num):
    champions.heroes.append(Hero(new_heroes[i]))

for i in range(0,num):
    the_winners.heroes.append(Hero(new_heroes[i]))

for hero in champions.heroes:
    new_armor = Armor(armors[random.randint(0,4)], armor_power)
    hero.add_armor(new_armor)
    new_ability = Ability(abilities[random.randint(0,4)], ability_power)
    hero.add_ability(new_ability)

for hero in the_winners.heroes:
    new_armor = Armor(armors[random.randint(0,4)], armor_power)
    hero.add_armor(new_armor)
    new_ability = Ability(abilities[random.randint(0,4)], ability_power)
    hero.add_ability(new_ability)

print(the_winners.heroes[3].armors[0].name)
print(the_winners.heroes[3].abilities[0].name)

print(champions.heroes[3].armors[0].name)
print(champions.heroes[3].abilities[0].name)

champions.attack(the_winners)
champions.attack(the_winners)
champions.stats()
the_winners.stats()
champions.attack(the_winners)
champions.stats()
the_winners.stats()






    # for i in range(0, 2)
    # team_one[i].add_armor(armors[i])
    #
    # team_one[i].add_ability(abilities[i])

# for i in range(0, num):
#     team_two.append(Hero(new_heroes[i]))
#     team_two[i].add_armor(armors[i])
#     team_two[i].add_ability(abilities[i])
#
# for hero in team_one:
#     champions.heroes.append(hero)
#
# for hero in team_two:
#     the_winners.heroes.append(hero)


# print(champions.heroes[0].name)
# print(the_winners.heroes[0].name)
#
# champions.attack(the_winners)
# print(the_winners.heroes[0])


# for hero in team_one:

# for i in range(0,num):


# team_one = Team("One")
# jodie = Hero("Jodie Foster")
# aliens = Ability("Alien Friends", 10000)
# jodie.add_ability(aliens)
# team_one.add_hero(jodie)
# team_two = Team("Two")
# athena = Hero("Athena")
# socks = Armor("Socks", 10)
# athena.add_armor(socks)
# team_two.add_hero(athena)
# team_one.attack(team_two)

# armor = Hero("The Ring", 200)
# print(armor.defend())

# big_strength = Ability("Overwhelming Strength", 30000)
# athena = Hero("Athena")
#     # assert athena.attack() == 0
# athena.add_ability(big_strength)
# attack = athena.attack()
# print(attack)

# >       assert attack <= 30000 and attack >= 15000

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
