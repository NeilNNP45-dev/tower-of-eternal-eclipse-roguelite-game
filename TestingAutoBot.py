BOT_CLASS = "Mage"
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
        target.health -= damage
        

    def strong_attack(self, target):
        if self.strong_attack_cooldown>0:
            return False
        damage = random.randint(self.strong_min, self.strong_max)
        crit = random.uniform(1, 100)
        if crit <= self.crit_chance:
            damage *= self.crit_multiplier
        target.health -= damage
         

class Knight(Character):
    def __init__(self, name):
        super().__init__(name, 140, 140, normal_min=5, normal_max=10, strong_min=15, strong_max=25, crit_chance=20, crit_multiplier=3, level=1, special_attack_cooldown = 5, special_attack_cooldown_turn = 5, accuracy = 100)
    def special_attack(self, target):
        if self.special_attack_cooldown>0:
            return False
        damage = random.randint(self.strong_min + 15, self.strong_max + 15)
        target.health -= damage
        self.health += 25
        self.health = min(self.health, self.max_health)
        return True  
            
class Mage(Character):
    def __init__(self, name):     
        super().__init__(name, 100, 100, normal_min=10, normal_max=15, strong_min=25, strong_max=35, crit_chance=5, crit_multiplier=5, level=1, special_attack_cooldown = 5, special_attack_cooldown_turn = 10, accuracy = 100)
    def special_attack(self, target):
        if self.special_attack_cooldown>0:
            
            return False
        damage = target.max_health
        target.health -= damage
        self.max_health -= int(self.max_health*0.25)
        self.health = min(self.health, self.max_health)
        return True      
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 100, 100, normal_min=7, normal_max=12, strong_min=18, strong_max=28, crit_chance=30, crit_multiplier=4, level=1, special_attack_cooldown = 5, special_attack_cooldown_turn = 3, accuracy = 100)
    def special_attack(self, target):
        self.accuracy = random.randint(1,100)
        if self.special_attack_cooldown>0:
        
            return False
        if self.accuracy <= 75:

         damage = random.randint(self.strong_min,self.strong_max)
         damage *= self.crit_multiplier + 1
         target.health -= damage
         return True
        else:
         damage = random.randint(max(1, self.normal_min//2), max(1,self.normal_max//2)) 
         target.health -= damage
         return True
      
def playerlevel_up(player):
    global saved_levels 
    player.level += 1
    saved_levels= player.level - 1
    if isinstance(player, Knight):
       player.max_health += 30
       player.health = player.max_health
       player.normal_min += 2
       player.normal_max += 2
       player.strong_min += 5
       player.strong_max += 5
    elif isinstance(player, Mage):
       player.max_health += 25
       player.health = player.max_health
       player.normal_min += 3
       player.normal_max += 3
       player.strong_min += 7
       player.strong_max += 7

    elif isinstance(player, Archer):
       player.max_health += 20
       player.health = player.max_health
       player.normal_min += 2
       player.normal_max += 2
       player.strong_min += 4
       player.strong_max += 4
       player.crit_chance += 0.5
       player.crit_chance = min(player.crit_chance, 75)
       
 

def enemylevel_up(enemy):
    enemy.level += 1
    enemy.max_health = int(enemy.max_health + wins* 5)
    enemy.health = enemy.max_health
    enemy.normal_min = int(enemy.normal_min + wins//3)
    enemy.normal_max = int(enemy.normal_max + wins//2)
    enemy.strong_min = int(enemy.strong_min + wins//3)
    enemy.strong_max = int(enemy.strong_max + wins//2)

def bosslevel_up(boss):
    if boss.name == "THE LOST PROTECTOR":
       boss.max_health += resets*25 + wins*2
       boss.health = boss.max_health
       boss.strong_min -= resets*2 
       boss.strong_max -= resets*2 

    elif boss.name == "THE LICH KING":
       boss.max_health += resets*15 + wins
       boss.health = boss.max_health
    
    elif boss.name == "THE HOLLOW HUMAN":
       boss.max_health += resets*20 + wins*2
       boss.health = boss.max_health
       

def auto_battle(player, enemy):

    while player.health > 0:

        # KNIGHT
        if isinstance(player, Knight):

            if player.special_attack_cooldown <= 0:
                player.special_attack(enemy)
                player.special_attack_cooldown = (
                    player.special_attack_cooldown_turn
                )
                player.strong_attack_cooldown -= 1

            elif player.strong_attack_cooldown <= 0:
                player.strong_attack(enemy)
                player.strong_attack_cooldown = 1
                player.special_attack_cooldown -= 1

            else:
                player.normal_attack(enemy)
                player.strong_attack_cooldown -= 1
                player.special_attack_cooldown -= 1

        # MAGE
        elif isinstance(player, Mage):

            if (
                enemy.max_health >= 425
                and player.special_attack_cooldown <= 0
            ):
                player.special_attack(enemy)
                player.special_attack_cooldown = (
                    player.special_attack_cooldown_turn
                )
                player.strong_attack_cooldown -= 1

            elif player.strong_attack_cooldown <= 0:
                player.strong_attack(enemy)
                player.strong_attack_cooldown = 1
                player.special_attack_cooldown -= 1

            else:
                player.normal_attack(enemy)
                player.strong_attack_cooldown -= 1
                player.special_attack_cooldown -= 1

        # ARCHER
        else:

            if player.special_attack_cooldown <= 0:
                player.special_attack(enemy)
                player.special_attack_cooldown = (
                    player.special_attack_cooldown_turn
                )
                player.strong_attack_cooldown -= 1

            elif player.strong_attack_cooldown <= 0:
                player.strong_attack(enemy)
                player.strong_attack_cooldown = 1
                player.special_attack_cooldown -= 1

            else:
                player.normal_attack(enemy)
                player.strong_attack_cooldown -= 1
                player.special_attack_cooldown -= 1

        if enemy.health <= 0:
            return True

        enemy_action = random.choice(
            ["normal", "strong"]
        )

        if (
            enemy_action == "strong"
            and enemy.strong_attack_cooldown <= 0
        ):
            enemy.strong_attack(player)
            enemy.strong_attack_cooldown = 1

        else:
            enemy.normal_attack(player)
            enemy.strong_attack_cooldown -= 1

        if player.health <= 0:
            return False
environments = {
    "The Forest of THE LOST ONES": {"Slime": 60, "Wolf": 100, "Bandits": 80},
    "The Dungeon of THE DEAD": {"Zombie": 60, "Orc": 120, "Skeleton": 80},
    "The Cave of THE HOLLOWS": {"Goblin": 70, "Ogre": 110, "Spider": 90}
}

env = random.choice(list(environments.keys()))
bosses = {
    "The Forest of THE LOST ONES": {"THE LOST PROTECTOR": {"max_health": 300, 
                                                      "normal_min": 30,
                                                      "normal_max": 50, 
                                                      "strong_min": -30, 
                                                      "strong_max": -10,
                                                      "crit_chance": 1,
                                                      "crit_multiplier": 2}},
    "The Dungeon of THE DEAD": {"THE LICH KING": {"max_health": 200,
                                                  "normal_min": 15,
                                                  "normal_max": 25,
                                                  "strong_min": 50,
                                                  "strong_max": 100,
                                                  "crit_chance": 0,
                                                  "crit_multiplier": 3.5}},
    "The Cave of THE HOLLOWS": {"THE HOLLOW HUMAN": {"max_health": 250,
                                                     "normal_min": 0, 
                                                     "normal_max": 0, 
                                                     "strong_min": 6, 
                                                     "strong_max": 10, 
                                                     "crit_chance": 100, 
                                                     "crit_multiplier": 10}}
}


player_name = "AUTOBOT"
saved_levels = 0
saved_exp = 0
saved_exp_needed = 100
resets = 0
while True:  
      wins = 0         
      exp =  saved_exp
      exp_needed = saved_exp_needed         
      if BOT_CLASS == "Knight":
        player = Knight(player_name)

      elif BOT_CLASS == "Mage":
        player = Mage(player_name)

      else:
        player = Archer(player_name)

      for i in range(saved_levels):
        playerlevel_up(player)
        
           

      while True:
       wins += 1
       if wins >= 51:
        print("\n===== SUCCESS =====")
        print(f"Class: {BOT_CLASS}")
        print(f"Resets: {resets}")
        print(f"Level: {player.level}")
        quit()

       if wins > 1:
        if wins % 5 == 0:
         print(
         f"Floor {wins} | "
         f"Level {player.level} | "
         f"Resets {resets}")
        env = random.choice(list(environments.keys()))
        boss_name = random.choice(list(bosses[env].keys()))
       if player.health < 50:
        player.health += 30
       if wins in [5, 10, 15, 20, 25, 30, 35, 40, 45, 55, 60, 65, 70, 75, 80, 85, 90, 95]:
            
             player.health = player.max_health
             boss = Character(boss_name, bosses[env][boss_name]
                              ["max_health"],
                                bosses[env][boss_name]["max_health"],
                                normal_min=bosses[env][boss_name]["normal_min"],
                                normal_max=bosses[env][boss_name]["normal_max"],
                                strong_min=bosses[env][boss_name]["strong_min"], 
                                strong_max=bosses[env][boss_name]["strong_max"],
                                crit_chance=bosses[env][boss_name]["crit_chance"],
                                crit_multiplier=bosses[env][boss_name]["crit_multiplier"])
             bosslevel_up(boss)
             if not auto_battle(player, boss):
                 saved_exp_needed = exp_needed
                 saved_exp = exp
                 resets += 1
                 break
             exp += random.randint(400 + resets*5 , 600 + resets*5)
             while exp >= exp_needed:
                 playerlevel_up(player)
                 exp -= exp_needed
                 exp_needed = int(exp_needed*1.3)
                
             player.health = player.max_health          
             continue           
       elif wins == 50:
             player.health = player.max_health
             boss = Character("THE FORGOTTEN ONE(SHADOW FORM)", 500, 500, normal_min=50, normal_max=70, strong_min=100, strong_max=150, crit_chance=50, crit_multiplier=5)
             if not auto_battle(player, boss):
                 saved_exp_needed = exp_needed
                 saved_exp = exp
                 resets += 1
                 break
             exp += random.randint(1000 + resets*5 , 1500 + resets*5)
             while exp >= exp_needed:
                 playerlevel_up(player)
                 exp -= exp_needed
                 exp_needed = int(exp_needed*1.3)
                
             player.health = player.max_health          
             continue           
       elif wins == 100:
               
                player.health = player.max_health
                boss = Character("THE FORGOTTEN ONE", 1000, 1000, normal_min=70, normal_max=100, strong_min=150, strong_max=250, crit_chance=75, crit_multiplier=5)
                if not auto_battle(player, boss):
                 saved_exp_needed = exp_needed
                 saved_exp = exp
                 resets += 1
                 break
                exp += random.randint(2500 + resets*5 , 3000 + resets*5)
                while exp >= exp_needed:
                    playerlevel_up(player)
                    exp -= exp_needed
                    exp_needed = int(exp_needed*1.3)
                player.health = player.max_health
                continue
       else:               
    
        enemy_name = random.choice(list(environments[env].keys()))
        enemy = Character(enemy_name, environments[env][enemy_name], environments[env][enemy_name], level = max(1, wins + random.randint(-1, 1)))
        enemylevel_up(enemy)
        if not auto_battle(player, enemy):
         saved_exp_needed = exp_needed
         saved_exp = exp
         resets += 1
         break

        exp += random.randint(100 + resets*5 , 150 + resets*5)
        while exp >= exp_needed:
            playerlevel_up(player)
            exp -= exp_needed
            exp_needed = int(exp_needed*1.3)
            
        if player.health <= 0:
          saved_exp_needed = exp_needed
          saved_exp = exp
          break

 