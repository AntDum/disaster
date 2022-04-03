import os

class Level:
    """
    A class dedicated to load and prepare the level for the Game Manager
    """

    def __init__(self,id):
        self.id = id
        self.grid = []
        self.size= 0
        with open(os.path.join("level","level"+str(id),"city.csv")) as f:
            for line in f:
                row = []
                self.size += 1
                for tile in line.strip().split(","):
                    row.append(tile)
                self.grid.append(row)
        self.score_tresholds = []
        self.cards = []
        self.best_score = 0
        self.name = "Panic city"
        with open(os.path.join("level","level"+str(id),"info")) as file:
            f = []
            for line in file:
                f.append(line.strip())
            self.name = f[0]
            self.score_tresholds = f[1].split(",")
            self.cards = [c.split(',') for c in f[2].split(";")]
            self.best_score = int(f[3])
            self.coasts = f[4].split(",")


    def report(self):
        return {"best_score":self.best_score,"tresholds":self.score_tresholds,"name":self.name, "cards":self.cards, "grid":self.grid, "size":self.size, "coasts" : self.coasts}

    def save_level(self,score):
        self.best_score = max(self.best_score,score)
        pass #TODO: finir la sauvegarde.

    def __str__(self):
        return f"LEVEL {self.id} : {self.name}\nBest score : {self.best_score}\nTresholds : {self.score_tresholds}\nCartes : {self.cards}"
