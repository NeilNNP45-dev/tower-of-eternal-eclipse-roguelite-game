from player import Knight,Mage,Archer
def playerlevel_up(player):
    player.level += 1
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
       

    print(f"{player.name} has leveled up to level {player.level}!") 

def enemylevel_up(enemy, wins):
    enemy.level += 1
    enemy.max_health = int(enemy.max_health + wins* 5)
    enemy.health = enemy.max_health
    enemy.normal_min = int(enemy.normal_min + wins//3)
    enemy.normal_max = int(enemy.normal_max + wins//2)
    enemy.strong_min = int(enemy.strong_min + wins//3)
    enemy.strong_max = int(enemy.strong_max + wins//2)

def bosslevel_up(boss, wins, resets):
    if boss.name == "THE LOST PROTECTOR":
       boss.max_health += resets*25 + wins*2
       boss.health = boss.max_health
       boss.strong_min -= resets*2 
       boss.strong_max -= resets*2 

    elif boss.name == "THE LICH KING":
       boss.max_health += resets*15 + wins*2
       boss.health = boss.max_health
    
    elif boss.name == "THE HOLLOW HUMAN":
       boss.max_health += resets*20 + wins*2
       boss.health = boss.max_health
