class Team:
    def __init__(self, name, score, rank):
        self.rank=rank
        self.name = name
        self.score=0
        self.winner=False 

    def getName(self):
        return self.name


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
        return self.name + "\nScore: " + str(self.score)

    def finalScores(self, lista):

        lista.sort(reverse=True)
        print(lista)
        return(lista)

team1 = Team('brasil', 0)
team1.finalScores([19,23,34,54,5,6,7,8,9,10,11,12])