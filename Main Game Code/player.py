import random
class Character:
    def __init__(self, name, health, max_health, normal_min=5, normal_max=10, strong_min=15, strong_max=25, crit_chance = 10, crit_multiplier = 2, level = 1, strong_attack_cooldown = 0, special_attack_cooldown = 0, special_attack_cooldown_turn = 0, accuracy = 100):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.normal_min = normal_min
        self.normal_max = normal_max
        self.strong_min = strong_min
        self.strong_max = strong_max
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier
        self.level = level
        self.strong_attack_cooldown = strong_attack_cooldown
        self.special_attack_cooldown = special_attack_cooldown
        self.special_attack_cooldown_turn = special_attack_cooldown_turn
        self.accuracy = accuracy

    def normal_attack(self, target):
        damage = random.randint(self.normal_min, self.normal_max)
        crit = random.uniform(1, 100)
        if crit <= self.crit_chance:
            damage *= self.crit_multiplier
            print(f"Critical hit!")
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
              

    def strong_attack(self, target):
        if self.strong_attack_cooldown>0:
            print(f"{self.name} cannot use strong attack this turn!")
            return False
        damage = random.randint(self.strong_min, self.strong_max)
        crit = random.uniform(1, 100)
        if crit <= self.crit_chance:
            damage *= self.crit_multiplier
            print(f"Critical hit!")
        target.health -= damage
        if damage < 0:
            print(f"{self.name} uses a strong attack on {target.name} but it heals them for {-damage} health!")
        else:
         print(f"{self.name} uses a strong attack on {target.name} for {damage} damage!")
        return True
        
class Knight(Character):
    def __init__(self, name):
        super().__init__(name, 140, 140, normal_min=5, normal_max=10, strong_min=15, strong_max=25, crit_chance=20, crit_multiplier=3, level=1, special_attack_cooldown = 5, special_attack_cooldown_turn = 5, accuracy = 100)
    def special_attack(self, target):
        if self.special_attack_cooldown>0:
            print(f"{self.name} cannot use Protector's Honour for {self.special_attack_cooldown} turns!")
            return False
        damage = random.randint(self.strong_min + 15, self.strong_max + 15)
        target.health -= damage
        self.health += 25
        self.health = min(self.health, self.max_health)
        print(f"{self.name} uses Protector's Honour")
        print(f"{target.name} takes {damage} damage!")
        print(f"{self.name} also heals by 25 HP")
        return True  
            
class Mage(Character):
    def __init__(self, name):     
        super().__init__(name, 100, 100, normal_min=10, normal_max=15, strong_min=25, strong_max=35, crit_chance=5, crit_multiplier=5, level=1, special_attack_cooldown = 5, special_attack_cooldown_turn = 10, accuracy = 100)
    def special_attack(self, target):
        if self.special_attack_cooldown>0:
            print(f"{self.name} cannot use Lich's Greed for {self.special_attack_cooldown} turns!")
            return False
        damage = target.max_health
        target.health -= damage
        self.max_health -= int(self.max_health*0.25)
        self.health = min(self.health, self.max_health)
        print(f"{self.name} uses Lich's Greed")
        print(f"{target.name} is ERASED FROM EXISTENCE...but at some COST!")
        print(f"{self.name} sacrificed a part of their life to erase the enemy's existence")
        return True      
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 100, 100, normal_min=7, normal_max=12, strong_min=18, strong_max=28, crit_chance=30, crit_multiplier=4, level=1, special_attack_cooldown = 5, special_attack_cooldown_turn = 3, accuracy = 100)
    def special_attack(self, target):
        self.accuracy = random.randint(1,100)
        if self.special_attack_cooldown>0:
            print(f"{self.name} cannot use HOLLOW's BARGAIN for {self.special_attack_cooldown} turns!")
            return False
        if self.accuracy <= 75:

         damage = random.randint(self.strong_min,self.strong_max)
         damage *= self.crit_multiplier + 1
         target.health -= damage
         print(f"{self.name} used Hollow's Bargain")
         print(f"{target.name} is HIT BY THE HOLLOWED ARROW!")
         return True
        else:
         damage = random.randint(max(1, self.normal_min//2), max(1,self.normal_max//2)) 
         target.health -= damage
         print(f"{self.name} used HOLLOW's BARGAIN...but they MISSED")
         print(f"THE HOLLOWED ARROW ONLY GRAZED THE {target.name}")
         return True 