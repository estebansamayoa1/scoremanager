class Team:
    def __init__(self, name, score):
        self.name = name
        self.score=score
        self.winner=False 

    def getName(self):
        return self.name

    def win(self):
        self.winner=True

    def __str__(self):
        return self.name + "\nScore: " + str(self.score)

