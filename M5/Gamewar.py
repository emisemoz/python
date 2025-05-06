import random
class Character:
    def __init__(self, char_type):
        self.char_type=char_type
        self.health= 0
        self.attack= 0
        self.dodge = 0
        self.assign_attributes()
    def assign_attributes(self):
        type_dict =  TYPES[self.char_type]
        self.health = type_dict["health"]
        self.attack = type_dict["attack"]
        self.dodge = type_dict["dodge"]

    def __str__(self):
        return self.char_type

    def attack_enemy(self):
        return self.attack

    def take_damage(self, damage):
        if self.dodge_success():
            return "Missed"
        self.health -= damage
        return f"{self.char_type} took {damage} damage"

    def dodge_success(self):
        dodge_chance = self.dodge * 5
        dodge_roll = random.randint(1, 100)
        return dodge_roll <= dodge_chance

    def is_dead(self):
        return self.health <= 0
    
class Character:
    def __init__(self, role):
        self.role = role
        self.health = 100
        self.attack_power = self.get_attack_power()
        self.dodge_chance = self.get_dodge_chance()

    def get_attack_power(self):
        role_attack = {
            "mage": 25,
            "warrior": 20,
            "archer": 15
        }
        return role_attack.get(self.role, 10)

    def get_dodge_chance(self):
        role_dodge = {
            "mage": 0.2,      # 20% chance to dodge
            "warrior": 0.1,   # 10% chance to dodge
            "archer": 0.3     # 30% chance to dodge
        }
        return role_dodge.get(self.role, 0.05)

    def attack_enemy(self):
        print(f"{self.role} attacks and deals {self.attack_power} damage.")
        return self.attack_power

    def take_damage(self, damage):
        if self.try_dodge():
            print(f"{self.role} dodged the attack!")
            return False  # did not take damage
        self.health -= damage
        print(f"{self.role} takes {damage} damage. Remaining health: {self.health}")
        return True  # damage was taken

    def try_dodge(self):
        return random.random() < self.dodge_chance

    def is_dead(self):
        return self.health <= 0

def attack_character(first, second):
    damage = first.attack_enemy()
    hit = second.take_damage(damage)
    if hit and second.is_dead():
        print(f"{second.role} has been defeated! {first.role} wins!")
        return True
    return False

def character_fight(type_1, type_2):
    character_1 = Character(type_1)
    character_2 = Character(type_2)

    coin_toss = random.randint(0, 1)
    if coin_toss == 0:
        first, second = character_1, character_2
        print("Player goes first.")
    else:
        first, second = character_2, character_1
        print("Computer goes first.")
    while True:
        if attack_character(first, second):
            break
        if attack_character(second, first):
            break