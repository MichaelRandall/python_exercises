#! /usr/bin/python

class Creature:
    def __init__(self, hit_points, weapon, color, sound):
        self.hit_points = hit_points
        self.weapon = weapon
        self.color = color
        self.sound = sound

    def battlecry(self):
        return self.sound.upper()

    
#from dunder_init import Creature

class Auto:
    def __init__(self, make = "Mercedes Benz", door_cnt = 4, color = "blue", auto_type = "sedan"):
        self.make = make
        self.door_cnt = door_cnt
        self.color = color
        self.auto_type = auto_type

#star star pulls out dictionary keywords values
class Animal:
    def __init__(self, **kwargs):
        self.feet_cnt = kwargs.get("feet_cnt", 4)
        self.size = kwargs.get("size", "small")
        self.sound = kwargs.get("sound", "squeak")
        self.skin = kwargs.get("skin", "fur")

    def attackcry(self):
        return self.sound.upper()

    def sorrycry(self):
        return self.sound.lower()
                                   
