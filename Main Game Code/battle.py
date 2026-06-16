import random
def battle(player, enemy, game_):
        while player.health > 0 :
            print(f"\n{player.name}'s Health: {player.health} | {enemy.name}'s Health: {enemy.health}")
            action = input("Choose your action (1: Normal Attack, 2: Strong Attack, 3: Special Attack, S: Save and Quit ): ")
            if action == '1':
                player.normal_attack(enemy)
                player.strong_attack_cooldown -= 1
                player.special_attack_cooldown -= 1
            elif action == '2':
                if  player.strong_attack_cooldown>0:
                    print(f"{player.name} cannot use strong attack this for {player.strong_attack_cooldown} turns!")
                    continue
                elif player.strong_attack(enemy):
                    player.strong_attack_cooldown =1
                    player.special_attack_cooldown -= 1
            elif action == '3':
                if player.special_attack_cooldown>0:
                 print(f"{player.name} cannot use their SPECIAL ATTACK for {player.special_attack_cooldown} turns!")
                 continue
                elif player.special_attack(enemy):
                    player.special_attack_cooldown = player.special_attack_cooldown_turn 
                    player.strong_attack_cooldown -= 1  
            elif action.lower() == "s":
                 print("Game Saved!")
                 return "save_quit"    
            else:
                print("Invalid action. Please choose again.")
                continue            

            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! You win!")
                return True

            enemy_action = random.choice(['normal', 'strong'])
            if enemy_action == 'strong' and enemy.strong_attack_cooldown==0:
                enemy.strong_attack(player)
                enemy.strong_attack_cooldown = 1 
            else:
                enemy.normal_attack(player)
                enemy.strong_attack_cooldown -= 1

        if player.health <= 0:
          print(f"{player.name} has been defeated! Game Over!")
          return False