import json

def save_game(game_state):
    data = {
        "saved_levels": game_state.saved_levels,
        "saved_exp": game_state.saved_exp,
        "saved_exp_needed": game_state.saved_exp_needed,
        "wins": game_state.wins,
        "resets": game_state.resets,
        "saved_class": game_state.saved_class
    }

    with open("save.json", "w") as file:
        json.dump(data, file, indent=4)

def load_game():
   try: 
    with open("save.json", "r") as file:
        data = json.load(file)

    return data      
   except FileNotFoundError:
      return None 