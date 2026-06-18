import random
from player import *
from battle import battle
from level_up import (playerlevel_up, enemylevel_up, bosslevel_up)   
from world import environments, bosses
from gamestate import GameState
from save_system import save_game, load_game

player_name = input("Enter your character's name: ")
game_state = GameState()
data = load_game()
if data:
 game_state.load_save(data)
 exp = game_state.saved_exp 
 exp_needed = game_state.saved_exp_needed
 print("Save Found")
 print(f"SAVED LEVELS = {game_state.saved_levels}")
 print(f"SAVED EXP = {game_state.saved_exp}")
 print(f"SAVED EXP NEEDED = {game_state.saved_exp_needed}")
 print(f"SAVED WINS = {game_state.wins}")
 print(f"SAVED RESETS = {game_state.resets}")
 print(f"SAVED CLASS = {game_state.saved_class}")
else:
 exp = 0
 exp_needed = 100
 print("No Save Found") 
current_floor = 0
while True:
 choices = input("Press A to Enter the Tower of Eternal Eclipse, Press Q to Quit): ")
 print("The Tower Remembers Your Previous Lives.......They weren't worthy enough")
 print(f"Current Life : {game_state.resets}")
 print("Don't Lose Too Many Lives" )
 if choices.lower() == 'a':  
       if game_state.saved_class:
        classes = game_state.saved_class
        print(f"Loaded Class: {classes}")
        if classes == "Knight":
         player = Knight(player_name)
         for i in range(game_state.saved_levels-1):
             playerlevel_up(player)    
        elif classes == "Mage":
         player = Mage(player_name)
         for i in range(game_state.saved_levels-1):
             playerlevel_up(player)    
        elif classes == "Archer":
         player = Archer(player_name)
         for i in range(game_state.saved_levels-1):
             playerlevel_up(player)    
        pass
       else:
        while True:     
         classes = input("Choose your class (1: Knight, 2: Mage, 3: Archer): ")
         if classes == '1':
            player = Knight(player_name)
            game_state.saved_class = "Knight"
            for i in range(game_state.saved_levels-1):
             playerlevel_up(player)    
            break
         elif classes == '2':
            player = Mage(player_name)
            game_state.saved_class = "Mage"
            for i in range(game_state.saved_levels-1):
             playerlevel_up(player)
            break
         elif classes == '3':
            player = Archer(player_name)
            game_state.saved_class = "Archer"
            for i in range(game_state.saved_levels-1):
             playerlevel_up(player)
            break
         else:
          print("Invalid class choice. Please choose again.")
       env = random.choice(list(environments.keys()))
       print(f"\nYou travel to the {env}.")
       boss_name = random.choice(list(bosses[env].keys()))
       while True:
          current_floor= game_state.wins + 1
          if game_state.wins > 1:
           env = random.choice(list(environments.keys()))
           boss_name = random.choice(list(bosses[env].keys()))
           print(f"\nYou travel to the {env}.")
          if player.health < 50:
           print(f"\nYou take a moment to rest and recover some health.")
           player.health += 30
          if current_floor in [5, 10, 15, 20, 25, 30, 35, 40, 45, 55, 60, 65, 70, 75, 80, 85, 90, 95]:
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
             bosslevel_up(boss, game_state)
             battle_result = battle(player, boss, game_state)
             if battle_result == "save_quit":
              game_state.saved_levels = player.level
              game_state.saved_exp = exp
              game_state.saved_exp_needed = exp_needed
              game_state.saved_class = classes
              save_game(game_state)
              print("Game Saved!")
              break
             if battle_result == False:
              game_state.saved_exp_needed = exp_needed
              game_state.saved_levels = player.level
              game_state.saved_exp = exp
              game_state.resets += 1
              game_state.wins = 0
              break
             exp += random.randint(400 + game_state.resets*5 , 600 + game_state.resets*5)
             while exp >= exp_needed:
                 playerlevel_up(player)
                 exp -= exp_needed
                 exp_needed = int(exp_needed*1.3)
             game_state.wins+=1     
             continue           
          elif current_floor == 50:
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
             battle_result = battle(player, boss, game_state)
             if battle_result == "save_quit":
              game_state.saved_levels = player.level
              game_state.saved_exp = exp
              game_state.saved_exp_needed = exp_needed
              game_state.saved_class = classes
              save_game(game_state)
              print("Game Saved!")
              break
             if battle_result == False:
              game_state.saved_exp_needed = exp_needed
              game_state.saved_levels = player.level
              game_state.saved_exp = exp
              game_state.resets += 1
              game_state.wins = 0
              break
             exp += random.randint(1000 + game_state.resets*5 , 1500 + game_state.resets*5)
             while exp >= exp_needed:
                 playerlevel_up(player)
                 exp -= exp_needed
                 exp_needed = int(exp_needed*1.3)
             game_state.wins+=1
                      
             continue           
          elif current_floor == 100:
                print(f"\n--- FINAL BOSS ---")
                print("You Rest Before Going in and Heal to Max")
                player.health = player.max_health
                print(f"Current Level: {player.level} | EXP: {exp}/{exp_needed}")
                print(f"\nThe Air Chills Around the Field as Something....SOMEONE POWERFUL Appears!")
                print(f"\n THE FORGOTTEN ONE emerges from the shadows!")
                print(f"\nThe Forgotten One says: 'You have proven yourself worthy, but can you defeat me?'")
                print(f"\n---THE FORGOTTEN ONE BOSS FIGHT---")
                boss = Character("THE FORGOTTEN ONE", 1000, 1000, normal_min=70, normal_max=100, strong_min=150, strong_max=250, crit_chance=75, crit_multiplier=5)
                battle_result = battle(player, boss, game_state)
                if battle_result == "save_quit":
                 game_state.saved_levels = player.level
                 game_state.saved_exp = exp
                 game_state.saved_exp_needed = exp_needed
                 game_state.saved_class = classes
                 save_game(game_state)
                 print("Game Saved!")
                 break
                if battle_result == False:
                 game_state.saved_exp_needed = exp_needed
                 game_state.saved_levels = player.level
                 game_state.saved_exp = exp
                 game_state.resets += 1
                 game_state.wins = 0
                 break
                exp += random.randint(2500 + game_state.resets*5 , 3000 + game_state.resets*5)
                while exp >= exp_needed:
                    playerlevel_up(player)
                    exp -= exp_needed
                    exp_needed = int(exp_needed*1.3)
                game_state.wins+=1     
                continue
          else:               
    
            print(f"\n--- Battle {current_floor} ---")
            print(f"Current Level: {player.level} | EXP: {exp}/{exp_needed}")
            enemy_name = random.choice(list(environments[env].keys()))
            enemy = Character(enemy_name, environments[env][enemy_name], environments[env][enemy_name], level = max(1, game_state.wins + random.randint(-1, 1)))
            enemylevel_up(enemy, game_state)
            print(f"\nA wild level {enemy.level} {enemy.name} appears!")
            battle_result = battle(player, enemy, game_state)
            if battle_result == "save_quit":
             game_state.saved_levels = player.level
             game_state.saved_exp = exp
             game_state.saved_exp_needed = exp_needed
             game_state.saved_class = classes
             save_game(game_state)
             print("Game Saved!")
             break
            if battle_result == False:
              game_state.saved_exp_needed = exp_needed
              game_state.saved_levels = player.level
              game_state.saved_exp = exp
              game_state.resets += 1
              game_state.wins = 0
              break

            exp += random.randint(100 + game_state.resets*5 , 150 + game_state.resets*5)
            while exp >= exp_needed:
             playerlevel_up(player)
             exp -= exp_needed
             exp_needed = int(exp_needed*1.3)
            game_state.wins+=1 

            if player.health <= 0:
             game_state.saved_exp_needed = exp_needed
             game_state.saved_exp = exp
             break

 elif choices.lower() == 'q':
        save_game(game_state)
        print("Thanks for playing!")
        break
 else:
        print("Invalid choice. Please choose again.")
        continue
   