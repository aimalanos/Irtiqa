import random
import math

class Creature:
    def __init__(self,square,level):
        self.location = square
        self.location.creature = self
        self.originalLocation = self.location
        self.level = level
        self.world = self.location.world
        self.health = random.randint(self.level*(7), self.level*(13))
        self.strength = random.randint(self.level*(3), self.level*(7))
        self.hostility = random.randint(self.level*(3), self.level*(7))
        self.speed = random.randint(self.level*(3), self.level*(7))
        self.fleeRate = random.uniform(0, 0.2)
        self.befriended = False
        self.experience = (self.health + self.strength + self.hostility + self.speed) // 3

class Wolf(Creature):
    def __init__(self,square,level):
        Creature.__init__(self,square,level)
        self.strength += 3*self.level
        self.hostility += 3*self.level
        self.speed -= 2*self.level
        if self.speed < 0: # No negative stats
            self.speed = 0
        self.fleeRate = self.fleeRate/2
        self.name = 'wolf'
class Tiger(Creature):
    def __init__(self,square,level):
        Creature.__init__(self,square,level)
        self.health += 4*self.level
        self.strength += 3*self.level
        self.hostility += 2*self.level
        self.speed += self.level
        self.name = 'tiger'
class Monkey(Creature):
    def __init__(self,square,level):
        Creature.__init__(self,square,level)
        self.health -= math.floor(10/level)
        self.strength += 2*self.level
        self.hostility += 3*self.level
        self.speed += 2*self.level
        self.fleeRate = self.fleeRate/2
        self.name = 'monkey'
class Dog(Creature):
    def __init__(self,square,level):
        Creature.__init__(self,square,level)
        self.strength += self.level
        self.hostility += random.randint(1,4)*self.level
        self.speed += self.level
        self.name = 'dog'
class Sheep(Creature):
    def __init__(self,square,level):
        Creature.__init__(self,square,level)
        self.health = math.floor(self.health*0.5)
        self.strength -= 15
        if self.strength < 1: # Strength must be at least 1
            self.strength = 1
        self.hostility -= 15
        if self.hostility < 1: # Hostility must be at least 1
            self.hostility = 1
        self.speed = 5
        self.fleeRate = 0.8
        self.name = 'sheep'
class Snake(Creature):
    def __init__(self,square,level):
        Creature.__init__(self,square,level)
        self.health = math.ceil(0.3*self.health)
        self.strength += 5*self.level
        self.hostility += 4*self.level
        self.speed *= 5
        self.fleeRate = self.fleeRate/2
        self.name = 'snake'
        
class Fish(Creature):
    def __init__(self,square,level):
        Creature.__init__(self,square,level)
        self.health = random.randint(self.level*(2), self.level*(5))
        self.strength = random.randint(self.level*(2), self.level*(4))
        self.hostility = random.randint(self.level*(2), self.level*(8))
        self.speed = random.randint(self.level*(2), self.level*(8))
        self.fleeRate = random.uniform(0, 0.5)
        self.name = 'fish'
        
class Eel(Creature):
    def __init__(self,square,level):
        Creature.__init__(self,square,level)
        self.health = random.randint(self.level*(5), self.level*(10))
        self.strength = random.randint(self.level*(5), self.level*(8))
        self.hostility = random.randint(self.level*(5), self.level*(8))
        self.speed = random.randint(self.level*(5), self.level*(8))
        self.name = 'eel'
        
class Leviathan(Creature):
    def __init__(self,square,level):
        Creature.__init__(self,square,level)
        self.health = random.randint(self.level*(10), self.level*(20))
        self.strength = random.randint(self.level*(5), self.level*(10))
        self.hostility = random.randint(self.level*(2), self.level*(6))
        self.speed = random.randint(self.level*(2), self.level*(6))
        self.fleeRate = 0
        self.experience = (self.health + self.strength + self.hostility + self.speed) // 2
        self.name = 'leviathan'
        
