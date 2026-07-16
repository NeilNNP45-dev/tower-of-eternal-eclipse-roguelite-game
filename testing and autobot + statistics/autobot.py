import random
import time

from statistics import save_run
from reports import generate_report
from csv_export import export_csv

BOT_CLASS = "Archer"
PLAYER_NAME = "AUTOBOT"

SHADOW_BOSS_FLOOR = 50
FINAL_BOSS_FLOOR = 100

BOSS_FLOORS = [
    5, 10, 15, 20, 25,
    30, 35, 40, 45,
    55, 60, 65, 70,
    75, 80, 85, 90, 95
]

class Character:
    def __init__(self, name, health, max_health, normal_min=5, normal_max=10, strong_min=15, strong_max=25, crit_chance = 10, crit_multiplier = 2, level = 1, strong_attack_cooldown = 0, special_attack_cooldown = 0, special_attack_cooldown_turn = 0, accuracy = 100,crit_data = 0, miss_data = 0,special_data = 0,normal_data = 0,strong_data = 0,total_damage_dealt = 0, total_damage_taken =  0):
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
        self.crit_data = crit_data
        self.miss_data = miss_data
        self.special_data = special_data
        self.normal_data = normal_data
        self.strong_data = strong_data
        self.total_damage_dealt = total_damage_dealt
        self.total_damage_taken = total_damage_taken

    def normal_attack(self, target):
        damage = random.randint(self.normal_min, self.normal_max)
        crit = random.uniform(1, 100)
        self.normal_data += 1
        if crit <= self.crit_chance:
             self.crit_data += 1
             damage *= self.crit_multiplier
        target.health -= damage
        self.total_damage_dealt += damage
        return damage

    def strong_attack(self, target):
        if self.strong_attack_cooldown > 0:
            return False
        damage = random.randint(self.strong_min, self.strong_max)
        crit = random.uniform(1, 100)
        self.strong_data += 1
        if crit <= self.crit_chance:
             self.crit_data += 1
             damage *= self.crit_multiplier
        target.health -= damage
        self.total_damage_dealt += damage
        return damage
       
class Knight(Character):
    def __init__(self, name):
        super().__init__(name, 140, 140, normal_min=5, normal_max=10, strong_min=15, strong_max=25, crit_chance=20, crit_multiplier=3, level=1, special_attack_cooldown = 5, special_attack_cooldown_turn = 5, accuracy = 100)
    def special_attack(self, target):
        if self.special_attack_cooldown > 0:
            return False
        damage = random.randint(self.strong_min + 15, self.strong_max + 15)
        target.health -= damage
        self.total_damage_dealt += damage
        self.health += 25
        self.health = min(self.health, self.max_health)
        self.special_data += 1
        return damage
          
class Mage(Character):
    def __init__(self, name):     
        super().__init__(name, 100, 100, normal_min=10, normal_max=15, strong_min=25, strong_max=35, crit_chance=5, crit_multiplier=5, level=1, special_attack_cooldown = 5, special_attack_cooldown_turn = 10, accuracy = 100)
    def special_attack(self, target):
        if self.special_attack_cooldown > 0:
            return False
        damage = target.max_health
        target.health -= damage
        self.total_damage_dealt += damage
        self.max_health -= int(self.max_health * 0.25)
        self.health = min(self.health, self.max_health)
        self.special_data += 1
        return damage     
    
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 100, 100, normal_min=7, normal_max=12, strong_min=18, strong_max=28, crit_chance=30, crit_multiplier=4, level=1, special_attack_cooldown = 5, special_attack_cooldown_turn = 3, accuracy = 100)
    def special_attack(self, target):
        self.accuracy = random.randint(1, 100)
        if self.special_attack_cooldown > 0:
            return False
        if self.accuracy <= 75:
            damage = random.randint(self.strong_min, self.strong_max)
            damage *= self.crit_multiplier + 1
            target.health -= damage
            self.total_damage_dealt += damage
            self.special_data += 1
            return damage
        else:
            damage = random.randint(max(1, self.normal_min // 2), max(1, self.normal_max // 2)) 
            self.miss_data += 1
            target.health -= damage
            self.total_damage_dealt += damage
            self.special_data += 1
            return damage
        
CLASS_MAP = {
    "Knight": Knight,
    "Mage": Mage,
    "Archer": Archer
}

def create_player():
    return CLASS_MAP[BOT_CLASS](PLAYER_NAME)

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
def auto_battle(player, enemy):
    battle_turn = 0
    while player.health > 0 and enemy.health > 0:
        # Player Actions
        if isinstance(player, Knight):
            if player.special_attack_cooldown <= 0:
                player.special_attack(enemy)
                battle_turn += 1
                player.special_attack_cooldown = player.special_attack_cooldown_turn
                player.strong_attack_cooldown -= 1
            elif player.strong_attack_cooldown <= 0:
                player.strong_attack(enemy)
                battle_turn += 1
                player.strong_attack_cooldown = 1
                player.special_attack_cooldown -= 1
            else:
                player.normal_attack(enemy)
                battle_turn += 1
                player.strong_attack_cooldown -= 1
                player.special_attack_cooldown -= 1

        elif isinstance(player, Mage):
            if enemy.max_health >= 1000 and player.special_attack_cooldown <= 0:
                player.special_attack(enemy)
                battle_turn += 1
                player.special_attack_cooldown = player.special_attack_cooldown_turn
                player.strong_attack_cooldown -= 1
            elif player.strong_attack_cooldown <= 0:
                player.strong_attack(enemy)
                battle_turn += 1
                player.strong_attack_cooldown = 1
                player.special_attack_cooldown -= 1
            else:
                player.normal_attack(enemy)
                battle_turn += 1
                player.strong_attack_cooldown -= 1
                player.special_attack_cooldown -= 1

        elif isinstance(player, Archer):
            if player.special_attack_cooldown <= 0:
                player.special_attack(enemy)
                battle_turn += 1
                player.special_attack_cooldown = player.special_attack_cooldown_turn
                player.strong_attack_cooldown -= 1
            elif player.strong_attack_cooldown <= 0:
                player.strong_attack(enemy)
                battle_turn += 1
                player.strong_attack_cooldown = 1
                player.special_attack_cooldown -= 1
            else:
                player.normal_attack(enemy)
                battle_turn += 1
                player.strong_attack_cooldown -= 1
                player.special_attack_cooldown -= 1

        if enemy.health <= 0:
            return True, battle_turn

        # Enemy Actions
        enemy_action = random.choice(["normal", "strong"])
        if enemy_action == "strong" and enemy.strong_attack_cooldown <= 0:
            damage = enemy.strong_attack(player)
            player.total_damage_taken += damage
            enemy.strong_attack_cooldown = 1                   
        else:
            damage = enemy.normal_attack(player)
            player.total_damage_taken += damage
            enemy.strong_attack_cooldown -= 1

        if player.health <= 0:
            return False, battle_turn

def enemylevel_up(enemy, wins):
    enemy.level += 1
    enemy.max_health = int(enemy.max_health + wins * 5)
    enemy.health = enemy.max_health
    enemy.normal_min = int(enemy.normal_min + wins // 3)
    enemy.normal_max = int(enemy.normal_max + wins // 2)
    enemy.strong_min = int(enemy.strong_min + wins // 3)
    enemy.strong_max = int(enemy.strong_max + wins // 2)

def bosslevel_up(boss, wins, resets):
    if boss.name == "THE LOST PROTECTOR":
        boss.max_health += resets * 25 + wins * 2
        boss.health = boss.max_health
        boss.strong_min -= resets * 2 
        boss.strong_max -= resets * 2 

    elif boss.name == "THE LICH KING":
        boss.max_health += resets * 15 + wins
        boss.health = boss.max_health
    
    elif boss.name == "THE HOLLOW HUMAN":
        boss.max_health += resets * 20 + wins * 2
        boss.health = boss.max_health             

environments = {
    "The Forest of THE LOST ONES": {"Slime": 60, "Wolf": 100, "Bandits": 80},
    "The Dungeon of THE DEAD": {"Zombie": 60, "Orc": 120, "Skeleton": 80},
    "The Cave of THE HOLLOWS": {"Goblin": 70, "Ogre": 110, "Spider": 90}
}

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

def run_simulation():
    saved_levels = 0
    saved_exp = 0
    saved_exp_needed = 100
    resets = 0
    wins = 0
    exp = saved_exp
    exp_needed = saved_exp_needed
    death_floor = []
    turns = []
    killer = []
    killer_type = [] 
    killer_health = []
    killer_health_percent = []
    total_damage_taken = []
    total_damage_dealt = []
    player = create_player()
    
    for _ in range(saved_levels):
        playerlevel_up(player)
        
    while True:
        wins += 1
        if wins > 1:
            env = random.choice(list(environments.keys()))
        if player.health < 50:
            player.health += 30    
    
        if wins in BOSS_FLOORS:
            player.health = player.max_health
            env = random.choice(list(environments.keys()))
            boss_name = random.choice(list(bosses[env].keys()))
            boss = Character(boss_name, bosses[env][boss_name]["max_health"],
                             bosses[env][boss_name]["max_health"],
                             normal_min=bosses[env][boss_name]["normal_min"],
                             normal_max=bosses[env][boss_name]["normal_max"],
                             strong_min=bosses[env][boss_name]["strong_min"], 
                             strong_max=bosses[env][boss_name]["strong_max"],
                             crit_chance=bosses[env][boss_name]["crit_chance"],
                             crit_multiplier=bosses[env][boss_name]["crit_multiplier"])
            bosslevel_up(boss, wins, resets)
            won, battle_turn = auto_battle(player, boss)
            if not won:
                saved_levels = player.level
                saved_exp = exp
                saved_exp_needed = exp_needed
                resets += 1
                death_floor.append(wins)
                turns.append(battle_turn)
                killer.append(boss.name)
                killer_type.append("Boss")
                killer_health.append(boss.health)
                killer_health_percent.append(round((boss.health / boss.max_health) * 100, 2))
                total_damage_taken.append(player.total_damage_taken)
                total_damage_dealt.append(player.total_damage_dealt)
            

                wins = 0
                player = create_player()
                for _ in range(saved_levels - 1):
                    playerlevel_up(player)
                exp = saved_exp
                exp_needed = saved_exp_needed
                continue

            exp += random.randint(400 + resets * 5, 600 + resets * 5)
            while exp >= exp_needed:
                playerlevel_up(player)
                exp -= exp_needed
                exp_needed = int(exp_needed * 1.3)  
            continue           
            
        elif wins == SHADOW_BOSS_FLOOR:
            player.health = player.max_health
            boss = Character("THE FORGOTTEN ONE(SHADOW FORM)", 500, 500, normal_min=50, normal_max=70, strong_min=100, strong_max=150, crit_chance=50, crit_multiplier=5)
            won, battle_turn = auto_battle(player, boss)
            if not won:
                saved_levels = player.level
                saved_exp = exp
                saved_exp_needed = exp_needed
                resets += 1
                death_floor.append(wins)
                turns.append(battle_turn)
                killer.append(boss.name)
                killer_type.append("Shadow Boss")
                killer_health.append(boss.health)
                killer_health_percent.append(round((boss.health / boss.max_health) * 100, 2))
                total_damage_taken.append(player.total_damage_taken)
                total_damage_dealt.append(player.total_damage_dealt)
                wins = 0
                player = create_player()
                for _ in range(saved_levels - 1):
                    playerlevel_up(player)
                exp = saved_exp
                exp_needed = saved_exp_needed
                continue

            exp += random.randint(1000 + resets * 5, 1500 + resets * 5)
            while exp >= exp_needed:
                playerlevel_up(player)
                exp -= exp_needed
                exp_needed = int(exp_needed * 1.3) 
            continue             
            
        elif wins == FINAL_BOSS_FLOOR:
            player.health = player.max_health
            boss = Character("THE FORGOTTEN ONE", 1000, 1000, normal_min=70, normal_max=100, strong_min=150, strong_max=250, crit_chance=75, crit_multiplier=5)
            won, battle_turn = auto_battle(player, boss)
            if not won:
                saved_levels = player.level
                saved_exp = exp
                saved_exp_needed = exp_needed
                resets += 1
                death_floor.append(wins)
                turns.append(battle_turn)
                killer.append(boss.name)
                killer_type.append("Final Boss")
                killer_health.append(boss.health)
                killer_health_percent.append(round((boss.health / boss.max_health) * 100, 2))
                total_damage_taken.append(player.total_damage_taken)
                total_damage_dealt.append(player.total_damage_dealt)
                wins = 0
                player = create_player()
                for _ in range(saved_levels - 1):
                    playerlevel_up(player)
                exp = saved_exp
                exp_needed = saved_exp_needed
                continue

            exp += random.randint(2500 + resets * 5, 3000 + resets * 5)
            while exp >= exp_needed:
                playerlevel_up(player)
                exp -= exp_needed
                exp_needed = int(exp_needed * 1.3)
            continue
            
        else: 
            env = random.choice(list(environments.keys()))              
            enemy_name = random.choice(list(environments[env].keys()))
            enemy = Character(enemy_name, environments[env][enemy_name], environments[env][enemy_name], level=max(1, wins + random.randint(-1, 1)))
            enemylevel_up(enemy, wins)   
            won, battle_turn = auto_battle(player, enemy)
            if not won:
                saved_levels = player.level
                saved_exp = exp
                saved_exp_needed = exp_needed
                resets += 1
                death_floor.append(wins)
                turns.append(battle_turn)
                killer.append(enemy.name)
                killer_type.append("Normal Enemy")
                killer_health.append(enemy.health)
                killer_health_percent.append(round((enemy.health / enemy.max_health) * 100, 2))
                total_damage_taken.append(player.total_damage_taken)
                total_damage_dealt.append(player.total_damage_dealt)
                wins = 0
                player = create_player()
                for _ in range(saved_levels - 1):
                    playerlevel_up(player)
                exp = saved_exp
                exp_needed = saved_exp_needed
                continue

            exp += random.randint(100 + resets * 5, 150 + resets * 5)
            while exp >= exp_needed:
                playerlevel_up(player)
                exp -= exp_needed
                exp_needed = int(exp_needed * 1.3) 
             
        if wins >=51:
            run_data = {
                "class": BOT_CLASS,
                "resets": resets,
                "level": player.level,
                "floor": wins,
                "death floor": death_floor,
                "turns": turns,
                "killer": killer,
                "killer type": killer_type,
                "killer health remaining": killer_health,
                "killer health percent": killer_health_percent,
                "total damage dealt": total_damage_dealt,
                "total damage taken": total_damage_taken,
                "crits": player.crit_data,
                "misses": player.miss_data,
                "normal_attacks": player.normal_data,
                "strong_attacks": player.strong_data,
                "special_attacks": player.special_data,
                "exp": exp
            }            
            return run_data

def main():
    sim_number = int(input("Enter Number of Simulations: "))
    start_time = time.perf_counter()

    for _ in range(sim_number):
        run_data = run_simulation()
        if run_data:
            save_run(run_data)
    generate_report()
    export_csv()

    end_time = time.perf_counter()
    print("Report generated successfully!")
    print(f"Execution Time: {end_time - start_time:.2f} seconds")     

if __name__ == "__main__":
    main()