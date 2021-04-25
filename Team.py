class Team:
    def __init__(self, name, score, rank):
        self.rank=rank 
        self.name = name
        self.score=0
        self.winner=False 

    def getName(self):
        return self.name

    def setRank(self, rank):
        self.rank=rank


    def setScore(self, score1, score2):
        if score1>score2:
            self.score+=3
        if score2>score1:
            self.score+=0
        if score1==score2:
            self.score+=1

    def getScore(self):
        return str(self.score)

    def __str__(self):
        return self.name + "\nScore: " + str(self.score)+"\nRank: "+str(self.rank)

