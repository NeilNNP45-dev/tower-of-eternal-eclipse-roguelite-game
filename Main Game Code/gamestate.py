class GameState:
    def __init__(self):
        self.saved_levels = 0
        self.saved_exp = 0
        self.saved_exp_needed = 100
        self.wins = 0
        self.resets =  0
        self.saved_class = None

    def load_save(self, data):
        self.saved_levels = data["saved_levels"]
        self.saved_exp = data["saved_exp"]
        self.saved_exp_needed = data["saved_exp_needed"]
        self.wins = data["wins"]
        self.resets = data["resets"]   
        self.saved_class = data["saved_class"] 