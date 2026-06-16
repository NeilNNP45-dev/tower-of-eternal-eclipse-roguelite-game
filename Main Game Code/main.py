import random
from player import *
from battle import battle
from level_up import (playerlevel_up, enemylevel_up, bosslevel_up)   
from world import environments, bosses


player_name = input("Enter your character's name: ")
saved_levels = 0
saved_exp = 0
saved_exp_needed = 100
resets = 0
while True:
 choices = input("Press A to Enter the Tower of Eternal Eclipse, Press Q to Quit): ")
 print("The Tower Remembers Your Previous Lives.......They weren't worthy enough")
 print(f"Current Life : {resets}")
 print("Don't Lose Too Many Lives" )
 if choices.lower() == 'a':    
      wins = 0         
      exp =  saved_exp
      exp_needed = saved_exp_needed  
      env = random.choice(list(environments.keys()))
      print(f"You find yourself in a {env}.")       
      while True:      
        classes = input("Choose your class (1: Knight, 2: Mage, 3: Archer): ")
        if classes == '1':
            player = Knight(player_name)
            for i in range(saved_levels):
             playerlevel_up(player)    
            break
        elif classes == '2':
            player = Mage(player_name)
            for i in range(saved_levels):
             playerlevel_up(player)
            break
        elif classes == '3':
            player = Archer(player_name)
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
             print("You Rest Before Going in and Heal to Max")
             player.health = player.max_health
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
             bosslevel_up(boss, wins, resets)
             if not battle(player, boss):
                 saved_exp_needed = exp_needed
                 saved_levels = player.level-1
                 saved_exp = exp
                 resets += 1
                 break
             exp += random.randint(400 + resets*5 , 600 + resets*5)
             while exp >= exp_needed:
                 playerlevel_up(player)
                 exp -= exp_needed
                 exp_needed = int(exp_needed*1.3)
                
             print(f"\nYou rest and recover to full health.")
             player.health = player.max_health          
             continue           
       elif wins == 50:
             print(f"\n--- FINAL BOSS ---")
             print("You Rest Before Going in and Heal to Max")
             player.health = player.max_health
             print(f"Current Level: {player.level} | EXP: {exp}/{exp_needed}")
             print(f"\nThe Air Chills Around the Field as Something....SOMEONE POWERFUL Appears!")
             print(f"\n THE FORGOTTEN ONE emerges from the shadows!") 
             print(f"\nThe Forgotten One says: 'You dare enter my domain? You arent good enough to fight me yet!'")
             print(f"\nThe Forgotten One leaves the field, but his shadow stays")
             print(f"\n---THE STRONGEST SHADOW BOSS FIGHT---")
             boss = Character("THE FORGOTTEN ONE(SHADOW FORM)", 500, 500, normal_min=50, normal_max=70, strong_min=100, strong_max=150, crit_chance=50, crit_multiplier=5)
             if not battle(player, boss):
                 saved_exp_needed = exp_needed
                 saved_levels = player.level-1
                 saved_exp = exp
                 resets += 1
                 break
             exp += random.randint(1000 + resets*5 , 1500 + resets*5)
             while exp >= exp_needed:
                 playerlevel_up(player)
                 exp -= exp_needed
                 exp_needed = int(exp_needed*1.3)
                 
             print(f"\nYou rest and recover to full health.")
             player.health = player.max_health          
             continue           
       elif wins == 100:
                print(f"\n--- FINAL BOSS ---")
                print("You Rest Before Going in and Heal to Max")
                player.health = player.max_health
                print(f"Current Level: {player.level} | EXP: {exp}/{exp_needed}")
                print(f"\nThe Air Chills Around the Field as Something....SOMEONE POWERFUL Appears!")
                print(f"\n THE FORGOTTEN ONE emerges from the shadows!")
                print(f"\nThe Forgotten One says: 'You have proven yourself worthy, but can you defeat me?'")
                print(f"\n---THE FORGOTTEN ONE BOSS FIGHT---")
                boss = Character("THE FORGOTTEN ONE", 1000, 1000, normal_min=70, normal_max=100, strong_min=150, strong_max=250, crit_chance=75, crit_multiplier=5)
                if not battle(player, boss):
                 saved_exp_needed = exp_needed
                 saved_levels = player.level-1
                 saved_exp = exp
                 resets += 1
                 break
                exp += random.randint(2500 + resets*5 , 3000 + resets*5)
                while exp >= exp_needed:
                    playerlevel_up(player)
                    exp -= exp_needed
                    exp_needed = int(exp_needed*1.3)
                print(f"\nYou rest and recover to full health.")
                player.health = player.max_health
                continue
       else:               
    
        print(f"\n--- Battle {wins} ---")
        print(f"Current Level: {player.level} | EXP: {exp}/{exp_needed}")
        enemy_name = random.choice(list(environments[env].keys()))
        enemy = Character(enemy_name, environments[env][enemy_name], environments[env][enemy_name], level = max(1, wins + random.randint(-1, 1)))
        enemylevel_up(enemy, wins)
        print(f"\nA wild level {enemy.level} {enemy.name} appears!")
        if not battle(player, enemy):
         saved_exp_needed = exp_needed
         saved_levels = player.level-1
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

 elif choices.lower() == 'q':
        print("Thanks for playing!")
        break
 else:
        print("Invalid choice. Please choose again.")
        continue
   