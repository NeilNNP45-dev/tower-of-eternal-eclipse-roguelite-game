import random
class Character:
    def __init__(self, name, health, max_health, normal_min=5, normal_max=10, strong_min=15, strong_max=25, crit_chance = 10, crit_multiplier = 2, level = 1):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.used_strong_last_turn = False
        self.normal_min = normal_min
        self.normal_max = normal_max
        self.strong_min = strong_min
        self.strong_max = strong_max
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier
        self.level = level

    def normal_attack(self, target):
        damage = random.randint(self.normal_min, self.normal_max)
        crit = random.randint(1, 100)
        if crit <= self.crit_chance:
            damage *= self.crit_multiplier
            print(f"Critical hit!")
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
              

    def strong_attack(self, target):
        if self.used_strong_last_turn:
            print(f"{self.name} cannot use strong attack this turn!")
            return False
        damage = random.randint(self.strong_min, self.strong_max)
        crit = random.randint(1, 100)
        if crit <= self.crit_chance:
            damage *= self.crit_multiplier
            print(f"Critical hit!")
        target.health -= damage
        self.used_strong_last_turn = True
        if damage < 0:
            print(f"{self.name} uses a strong attack on {target.name} but it heals them for {-damage} health!")
        else:
         print(f"{self.name} uses a strong attack on {target.name} for {damage} damage!")
        return True
        
class Knight(Character):
     def __init__(self, name):
        super().__init__(name, 120, 120, normal_min=5, normal_max=10, strong_min=15, strong_max=25, crit_chance=20, crit_multiplier=3, level=1)
        
class Mage(Character):
    def __init__(self, name):     
        super().__init__(name, 80, 80, normal_min=8, normal_max=15, strong_min=20, strong_max=35, crit_chance=5, crit_multiplier=5, level=1)
        
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 100, 100, normal_min=7, normal_max=12, strong_min=18, strong_max=28, crit_chance=100, crit_multiplier=4, level=1)

def playerlevel_up(player):
    global saved_levels
    player.level += 1
    saved_levels += 1
    player.max_health += 5
    player.health = player.max_health
    player.normal_min += 2
    player.normal_max += 2
    player.strong_min += 5
    player.strong_max += 5
    print(f"{player.name} has leveled up to level {player.level}!") 

def enemylevel_up(enemy):
    enemy.level += 1
    enemy.max_health = int(enemy.max_health + enemy.level* 10)
    enemy.health = enemy.max_health
    enemy.normal_min = int(enemy.normal_min + enemy.level * 0.5)
    enemy.normal_max = int(enemy.normal_max + enemy.level * 1.5)
    enemy.strong_min = int(enemy.strong_min + enemy.level * 0.5)
    enemy.strong_max = int(enemy.strong_max + enemy.level * 1.5)

def battle(player, enemy):
        while player.health > 0 :
            print(f"\n{player.name}'s Health: {player.health} | {enemy.name}'s Health: {enemy.health}")
            action = input("Choose your action (1: Normal Attack, 2: Strong Attack): ")
            if action == '1':
                player.normal_attack(enemy)
                player.used_strong_last_turn = False
            elif action == '2':
                if  player.used_strong_last_turn == True:
                    print(f"{player.name} cannot use strong attack this turn!")
                    continue
                elif player.strong_attack(enemy):
                    player.used_strong_last_turn = True
                    
            else:
                print("Invalid action. Please choose again.")
                continue            

            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! You win!")
                return True

            enemy_action = random.choice(['normal', 'strong'])
            if enemy_action == 'strong' and not enemy.used_strong_last_turn == True:
                enemy.strong_attack(player)

            else:
                enemy.normal_attack(player)
                enemy.used_strong_last_turn = False

        if player.health <= 0:
          print(f"{player.name} has been defeated! Game Over!")
          return False

environments = {
    "The Forest of THE LOST ONES": {"Slime": 60, "Wolf": 100, "Bandits": 80},
    "The Dungeon of THE DEAD": {"Zombie": 60, "Orc": 120, "Skeleton": 80},
    "The Cave of THE HOLLOWS": {"Goblin": 70, "Ogre": 110, "Spider": 90}
}

env = random.choice(list(environments.keys()))
print(f"You find yourself in a {env}.")
bosses = {
    "The Forest of THE LOST ONES": {"THE LOST PROTECTOR": {"max_health": 350, 
                                                      "normal_min": 30,
                                                      "normal_max": 50, 
                                                      "strong_min": -30, 
                                                      "strong_max": -10,
                                                      "crit_chance": 1,
                                                      "crit_multiplier": 2}},
    "The Dungeon of THE DEAD": {"THE LICH KING": {"max_health": 250,
                                                  "normal_min": 15,
                                                  "normal_max": 25,
                                                  "strong_min": 75,
                                                  "strong_max": 100,
                                                  "crit_chance": 0,
                                                  "crit_multiplier": 3.5}},
    "The Cave of THE HOLLOWS": {"THE HOLLOW HUMAN": {"max_health": 300,
                                                     "normal_min": 0, 
                                                     "normal_max": 0, 
                                                     "strong_min": 10, 
                                                     "strong_max": 15, 
                                                     "crit_chance": 100, 
                                                     "crit_multiplier": 10}}
}


player_name = input("Enter your character's name: ")
saved_levels = 0
while True:
 choices = input("Press A to Enter the Tower of Eternal Eclipse, Press Q to Quit): ")
 if choices.lower() == 'a':    
      wins = 0         
      exp =  0
      exp_needed = 100          
      while True:      
        classes = input("Choose your class (1: Knight, 2: Mage, 3: Archer): ")
        if classes == '1':
            player = Knight(player_name)
            print(saved_levels)
            for i in range(saved_levels):
             playerlevel_up(player)    
             break
        elif classes == '2':
            player = Mage(player_name)
            print(saved_levels)
            for i in range(saved_levels):
             playerlevel_up(player)
            break
        elif classes == '3':
            player = Archer(player_name)
            print(saved_levels)
            for i in range(saved_levels):
             playerlevel_up(player)
            break
        else:
            print("Invalid class choice. Please choose again.")
        
           

      while True:
       wins += 1
       if wins > 1:
        env = random.choice(list(environments.keys()))
        boss_name = random.choice(list(bosses[env].keys()))
        print(f"\nYou travel to the {env}.")
       if player.health < 50:
        print(f"\nYou take a moment to rest and recover some health.")
        player.health += 30
       if wins in [5, 10, 15, 20, 25, 30, 35, 40, 45, 55, 60, 65, 70, 75, 80, 85, 90, 95]:
             print(f"\n--- BOSS ROOM ---")
             print(f"Current Level: {player.level} | EXP: {exp}/{exp_needed}")
             print(f"\nA powerful boss appears!")
             boss = Character(boss_name, bosses[env][boss_name]
                              ["max_health"],
                                bosses[env][boss_name]["max_health"],
                                normal_min=bosses[env][boss_name]["normal_min"],
                                normal_max=bosses[env][boss_name]["normal_max"],
                                strong_min=bosses[env][boss_name]["strong_min"], 
                                strong_max=bosses[env][boss_name]["strong_max"],
                                crit_chance=bosses[env][boss_name]["crit_chance"],
                                crit_multiplier=bosses[env][boss_name]["crit_multiplier"])
             if not battle(player, boss):
                 break
             exp += 500
             while exp >= exp_needed:
                 playerlevel_up(player)
                 exp -= exp_needed
                 exp_needed = int(exp_needed*1.5)
             print(f"\nYou rest and recover to full health.")
             player.health = player.max_health          
             continue           
       elif wins == 50:
             print(f"\n--- FINAL BOSS ---")
             print(f"Current Level: {player.level} | EXP: {exp}/{exp_needed}")
             print(f"\nThe Air Chills Around the Field as Something....SOMEONE POWERFUL Appears!")
             print(f"\n THE FORGOTTEN ONE emerges from the shadows!") 
             print(f"\nThe Forgotten One says: 'You dare enter my domain? You arent good enough to fight me yet!'")
             print(f"\nThe Forgotten One leaves the field, but his shadow stays")
             print(f"\n---THE STRONGEST SHADOW BOSS FIGHT---")
             boss = Character("THE FORGOTTEN ONE(SHADOW FORM)", 500, 500, normal_min=50, normal_max=70, strong_min=100, strong_max=150, crit_chance=50, crit_multiplier=5)
             if not battle(player, boss):
                 break
             exp += 1000
             while exp >= exp_needed:
                 playerlevel_up(player)
                 exp -= exp_needed
                 exp_needed = int(exp_needed*1.5)
             print(f"\nYou rest and recover to full health.")
             player.health = player.max_health          
             continue           
       elif wins == 100:
                print(f"\n--- FINAL BOSS ---")
                print(f"Current Level: {player.level} | EXP: {exp}/{exp_needed}")
                print(f"\nThe Air Chills Around the Field as Something....SOMEONE POWERFUL Appears!")
                print(f"\n THE FORGOTTEN ONE emerges from the shadows!")
                print(f"\nThe Forgotten One says: 'You have proven yourself worthy, but can you defeat me?'")
                print(f"\n---THE FORGOTTEN ONE BOSS FIGHT---")
                boss = Character("THE FORGOTTEN ONE", 1000, 1000, normal_min=70, normal_max=100, strong_min=150, strong_max=250, crit_chance=75, crit_multiplier=5)
                if not battle(player, boss):
                 break
                exp += 2500
                while exp >= exp_needed:
                    playerlevel_up(player)
                    exp -= exp_needed
                    exp_needed = int(exp_needed*1.5)
                print(f"\nYou rest and recover to full health.")
                player.health = player.max_health
                continue
       else:               
    
        print(f"\n--- Battle {wins} ---")
        print(f"Current Level: {player.level} | EXP: {exp}/{exp_needed}")
        enemy_name = random.choice(list(environments[env].keys()))
        enemy = Character(enemy_name, environments[env][enemy_name], environments[env][enemy_name], level = max(1, player.level + random.randint(-1, 1)))
        enemylevel_up(enemy)
        print(f"\nA wild level {enemy.level} {enemy.name} appears!")
        if not battle(player, enemy):
         break

        exp += 100
        while exp >= exp_needed:
            playerlevel_up(player)
            exp -= exp_needed
            exp_needed = int(exp_needed*1.5)
            
        if player.health <= 0:
          break

 elif choices.lower() == 'q':
        print("Thanks for playing!")
        break
 else:
        print("Invalid choice. Please choose again.")
        continue
   