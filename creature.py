#! /usr/bin/python

#Allows/requires users to specify values when they instantiate this object
class Creature_One:
    def __init__(self, hit_points, weapon, color, sound):
        self.hit_points = hit_points
        self.weapon = weapon
        self.color = color
        self.sound = sound

    def battlecry(self):
        return self.sound.upper()

#usage:
#my_creature = Creature_One(20,"broom","yellow","scratch")
#return my_creature.color

#=========================================================================


#Allows users to specify values different than the defaults when the instantiate this object
class Creature_Two:
    def __init__(self, hit_points=10, weapon="spear", color="green", sound="woof"):
        self.hit_points = hit_points
        self.weapon = weapon
        self.color = color
        self.sound = sound

    def battlecry(self):
        return self.sound.upper()

#The same as above use uses the **kwargs for more efficiency
class Creature_Three:
    def __init__(self, **kwargs):
        self.hit_points = kwargs.get("hit_points", 100)
        self.weapon = kwargs.get("weapon", "baseball bat")
        self.color = kwargs.get("color", "purple")
        self.sound = kwargs.get("sound", "meow")

    def battlecry(self):
        return self.sound.upper()


#usage:
#my_creature = Creature_Three(hit_points=50)
#return my_creature.hit_points
#==========================================================================
    
import random

COLORS = ['red', 'green', 'blue', 'orange']

class Creature_Four:
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = "spear"
    sound = "ahhhhh"

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points) #defaults
        self.experience = random.randint(self.min_experience, self.max_experience) #defaults
        self.color = random.choice(COLORS) #defaults

        for key, value in kwargs.items():
            setattr(self, key, value)

#usage
#big_creature = Creature_Four(color="purple", sound="snort" adjective="horrifying")
#return big_creature.sound
#=================================================================================
