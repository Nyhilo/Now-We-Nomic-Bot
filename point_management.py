#
import random

# Can you say, "Object Oriented"?
class Item(object):
    def __init__(self, name, creator, cost=0, sellprice=0, amount=1, notes=""):
        self.name      = name
        self.creator   = creator
        self.cost      = cost
        self.sellprice = sellprice
        self.amount    = amount
        self.notes     = notes

class Player(object):
    def __init__(self, name, points=0, nc=2000, inventory=[]):
        self.name      = name
        self.points    = points
        self.nc        = nc
        self.inventory = []

    def indexOf(self, item):
        return self.inventory.index(item)

    def addItem(self, item, number=1):
        if item in self.inventory:
            self.inventory[ self.indexOf(item) ].amount += number
        else:
            self.inventory.append(item)
        return str(number) + " " + item.name + " added!"

    def removeItem(self, item):
        if item in self.inventory:
            index = self.indexOf(item)
            if self.inventory[index].amount > 1:
                self.inventory[index].amount -= 1
                return "One " + item.name + " removed!"
            else:
                self.inventory.pop(index)
            return item.name + " removed!"
        else:
            return self.name + " doesn't own any " + item.name + "!"

class PlayerDict(object):
    def __init__(self, players={}):
        self.players = players


class TurnList(object):
    def __init__(self, filename="", players=[]):
        self.players = players
        self.filename = filename

    def load(self):
        output = []
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                count = 0
                for line in lines:
                    count += 1
                    line = line.split(',')
                    if len(line) != 3:
                        print("Skipping line " + str(count) + " during playerlist load.")
                    else:
                        try:
                            output.append(Player(name=line[0],
                                                 points=float(line[1]),
                                                 nc=int(line[2]) ))
                        except ValueError:
                            print("Line " + str(count) + "malformattedin playerlist.")
            return output

        except FileNotFoundError:
            file = open(self.filename, 'w')
            file.close()
            print("playerlist file created.")
            return []

    def save(self):
        lines = ""
        for player in self.players:
            lines += player.name + "," + str(player.points) + "," + str(player.nc) + "\n"
        with open(self.filename, 'w') as file:
            file.write(lines)

    def findPlayerIndex(self, playername):
        for player in self.players:
            if player.name == playername:
                return self.players.index(player)
        return None

    def addPlayer(self, playername):
        self.players.append(Player(name=playername))
        return playername + " added to the roster."

    def removePlayer(self, playername):
        player = self.findPlayerIndex(playername)
        if player == None:
            return "No player by that name found."
        else:
            self.players.pop(player)
            return playername + " removed from the game."

    def givePoints(self, playername, points):
        player = self.findPlayerIndex(playername)
        if player == None:
            return "No player by that name found."
        else:
            try:
                self.players[player].points += float(points)
            except ValueError:
                return "Please enter a number for points, e.g. `!points @playername#0000 8`"

    def giveNc(self, playername, nc):
        player = self.findPlayerIndex(playername)
        if player == None:
            return "No player by that name found."
        else:
            try:
                self.players[player].nc += float(nc)
            except ValueError:
                return "Please enter a number for nc, e.g. `!nc @playername#0000 8`"


    def roster(self):
        roster = "```md\n  {:20}{:>6}{:>12}\n\n".format("Player","Score","nc")
        lead = ">"
        for player in self.players:
            roster += lead + " {:20}{:>6g}{:>12}\n".format(
                player.name.split('#')[0], player.points, player.nc)

            if lead == " ":
                lead = ">"
            else:
                lead = " "
        roster += "\n```"

        return roster


