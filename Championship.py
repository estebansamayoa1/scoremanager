from Team import Team
from Linked_List import LinkedList, Node
class Championship:
    def __init__(self, name, teams, winner):
        self.name=name
        self.teams = LinkedList()
        self.winner=None

    def newChampTeam(self, teams):
        self.teams = teams

    def getChampName(self):
        return self.name
    
    def newteam(self, nuevo):
        self.teams+=nuevo
    
    def getTeams(self):
        return self.teams