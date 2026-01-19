class Player:
    def __init__(self, race, name): #Defining the Player
        self.race = race
        self.name = name
        self.health = 100

    def get_race(self): 
        return self.race
    
    def set_race(self, race): #Options for races to choose from
        allowed_races = ["whit", "blat", "asi", "mex"]
        if race in allowed_races:
            self.race = race
        else:
            raise ValueError(f"Race must be one of: {allowed_races}")


    

