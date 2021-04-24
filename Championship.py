from Team import Team
class Championship:
    def __init__(self, name, teams, winner):
        self.name=name
        self.teams=teams
        self.winner=None


    def newteam(self, nuevo):
        self.teams+=nuevo