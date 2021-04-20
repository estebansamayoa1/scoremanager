class Team:
    def __init__(self, name, size, score):
        self.name = name
        self.size = size
        self.score=score
        self.winner=False 

    def win(self):
        self.winner=True

