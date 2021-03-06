from Square import Square
import Creature
import random

class World:
    terrains = ['forest','desert','desert','hills','hills','lake','tundra','grassy','grassy'] # Some of the terrains are in here twice so that they'll be more likely
    landItems = ['sticky sap', 'poison berries', 'big leaf', 'healing salve', 'flowers', 'big stick', 'nesting materials']
    waterItems = ['seaweed','driftwood','conch shell']
    itemWeights = {'fruit': 2, 'meat': 2, 'sticky sap': 3, 'poison berries': 3, 'big leaf': 3, 'healing salve': 3, 'flowers': 2, 'big stick': 3, 'nesting materials': 5, 'conch shell': 2, 'driftwood': 5, 'seaweed': 2}
    possibleCreatures = [Creature.Wolf,Creature.Tiger,Creature.Monkey,Creature.Dog,Creature.Sheep,Creature.Snake]
    creatureNames = ['wolf','tiger','monkey','dog','sheep','snake']
    aquaticCreatures = [Creature.Fish,Creature.Eel,Creature.Leviathan]
    weatherlist = ["clear", "rainy", "hailing", "snowy", "drought"]
    
    def __init__(self):
        self.turn_count = 0
        self.weather = "clear"
        self.player = None
        self.squares = []
        self.possibleCommands = {'me':['me'],'help':['help'],'allstats':['allstats','all stats'],'pickup':['pickup','pick up'],'go':['go'],'inspect':['inspect'], 'attack': ['attack','fight'], 'befriend': ['befriend'], 'recruit': ['recruit'], 'dismiss':['dismiss'], 'evolve': ['evolve'], 'use': ['use'], 'inventory': ['inventory'], 'drop': ['drop']}
        self.weather = 'clear'
        self.mapx = 8
        self.mapy = 8
        self.hostilityDec = False
        self.hostilityTime = 0
        
    def makeMap(self,x,y):
        for i in range(x+1):
            for j in range(y+1):
                self.squares.append(Square(self, i, j))
        for squ in self.squares:
            t = random.randint(0,8)
            squ.terrain = self.terrains[t] # We randomly assign terrains to squares
            if squ.exits['east'] == None: # If the square doesn't yet have an east exit, then we add one
                if squ.coordinates[0] != 2*x: # The eastmost squares won't have an east exit
                    for squ2 in self.squares:
                        if squ2.coordinates[0] == squ.coordinates[0] + 1:
                            if squ2.coordinates[1] == squ.coordinates[1]:
                                squ.exits['east'] = squ2
                                squ2.exits['west'] = squ
            if squ.exits['west'] == None: # If the square doesn't yet have a west exit, then we add one
                if squ.coordinates[0] != 0: # The westmost squares won't have a west exit
                    for squ2 in self.squares:
                        if squ2.coordinates[0] == squ.coordinates[0] - 1:
                            if squ2.coordinates[1] == squ.coordinates[1]:
                                squ.exits['west'] = squ2
                                squ2.exits['east'] = squ
            if squ.exits['north'] == None: # If the square doesn't yet have a north exit, then we add one
                if squ.coordinates[1] != 2*y: # The northmost squares won't have a north exit
                    for squ2 in self.squares:
                        if squ2.coordinates[1] == squ.coordinates[1] + 1:
                            if squ2.coordinates[0] == squ.coordinates[0]:
                                squ.exits['north'] = squ2
                                squ2.exits['south'] = squ
            if squ.exits['south'] == None: # If the square doesn't yet have a south exit, then we add one
                if squ.coordinates[0] != 0: # The southmost squares won't have a south exit
                    for squ2 in self.squares:
                        if squ2.coordinates[1] == squ.coordinates[1] - 1:
                            if squ2.coordinates[0] == squ.coordinates[0]:
                                squ.exits['south'] = squ2
                                squ2.exits['north'] = squ
                                
    def showMap(self):
        sWidth = 8 #square width
        sHeight = 4
        print('|' + ('-'*sWidth + '|')*(self.mapx+1)) #top border
        row = self.mapy #start here to get proper north/south orientation
        while row >= 0: #go from self.mapy to 0
            curr = [] #keeps track of all square objects in current row
            minirow = 0 #aka sub-row; tracks lines within the square
            while minirow < sHeight:
                if minirow == 0: #top line of each square states terrain
                    for elem in self.squares:
                        if elem.coordinates[1] == row: #all squares with y-coord equal to current row are relevant
                            curr.append(elem)          #add these squares to curr
                    print('| ' + curr[0].terrain + ' '*(sWidth-len(curr[0].terrain)-1) + '| ' + curr[1].terrain + ' '*(sWidth-len(curr[1].terrain)-1) + '| ' + curr[2].terrain + ' '*(sWidth-len(curr[2].terrain)-1) + '| ' + curr[3].terrain + ' '*(sWidth-len(curr[3].terrain)-1) + '| ' + curr[4].terrain + ' '*(sWidth-len(curr[4].terrain)-1) + '| ' + curr[5].terrain + ' '*(sWidth-len(curr[5].terrain)-1) + '| ' + curr[6].terrain + ' '*(sWidth-len(curr[6].terrain)-1) + '| ' + curr[7].terrain + ' '*(sWidth-len(curr[7].terrain)-1) + '| ' + curr[8].terrain + ' '*(sWidth-len(curr[8].terrain)-1) + '|')
                    minirow += 1
                elif minirow == 1:
                    if self.player.location.coordinates[1] == row:
                        print('|' + (' '*sWidth + '|')*self.player.location.coordinates[0] + '   YOU  |' + (' '*sWidth + '|')*(self.mapx-self.player.location.coordinates[0]))
                        minirow += 1
                    elif self.player.home.coordinates[1] == row: #display home location
                        print('|' + (' '*sWidth + '|')*self.player.home.coordinates[0] + '  HOME  |' + (' '*sWidth + '|')*(self.mapx-self.player.home.coordinates[0]))
                        minirow += 1
                    else:
                        print('|' + (' '*sWidth + '|')*(self.mapx+1))
                        minirow += 1
                elif minirow == 2: #minirow 2 is just spaces
                    if self.player.location.coordinates[1] == row:
                        print('|' + (' '*sWidth + '|')*self.player.location.coordinates[0] + 'ARE HERE|' + (' '*sWidth + '|')*(self.mapx-self.player.location.coordinates[0]))
                        minirow += 1
                    else:
                        print('|' + (' '*sWidth + '|')*(self.mapx+1))
                        minirow += 1
                else: #minirow 3 is the bottom border of each square
                    print('|' + ('-'*sWidth + '|')*(self.mapx+1))
                    minirow += 1
                    if minirow == 4:
                        row -= 1
                        break

    def add_player(self, player):
        self.player = player
        
    def update(self):
        self.player.update()
        self.turn_count += 1
        if self.turn_count % 5 == 0: # Every five turns...
            # New creatures will spawn
            randomSquare = random.choice(self.squares)
            if randomSquare.creature == None and randomSquare != self.player.home:
                level = random.randint(1,3)
                creatureType = random.choice(self.possibleCreatures)
                creatureType(randomSquare, level)
            # New food will appear
            for i in range(3):
                randomSquare = random.choice(self.squares)
                if 'fruit' in randomSquare.items:
                    randomSquare.items['fruit'] += 1
                else:
                    randomSquare.items['fruit'] = 1
            # New items will appear
            for i in range(2):
                randomSquare = random.choice(self.squares)
                if randomSquare.terrain == 'lake':
                    newItem = random.choice(self.waterItems)
                    if newItem in randomSquare.items:
                        randomSquare.items[newItem] += 1
                    else:
                        randomSquare.items[newItem] = 1
                else:
                    newItem = random.choice(self.landItems)
                    if newItem in randomSquare.items:
                        randomSquare.items[newItem] += 1
                    else:
                        randomSquare.items[newItem] = 1
            # The weather will change
            self.weather = random.choice(self.weatherlist)
            if self.weather == 'rainy' or self.weather == 'snowy' or self.weather == 'hailing':
                if self.player.location.terrain == 'desert': # It's not going to be rainy, snowy, or hailing in the desert
                    self.weather = 'clear'
            elif self.weather == 'drought': # There's not going to be a drought in the tundra
                if self.player.location.terrain == 'tundra':
                    self.weather = 'clear'
        if self.hostilityDec == True:
            if self.hostilityTime >= 2:
                self.hostilityDec = False
            for square in self.squares:
                if square.creature != None:
                    square.creature.hostility -= 1
            self.hostilityTime += 1
        for square in self.squares:
            if square.creature != None:
                if square.creature.hostility < 0:
                    square.creature.hostility = 0
