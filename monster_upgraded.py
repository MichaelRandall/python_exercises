#! /usr/bin/python


import random

COLORS = ['yellow','blue','red','green','orange']

class Monster(object):
    min_hit_pts = 1
    max_hit_pts = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'snort'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_pts, self.max_hit_pts)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def battlecry(self):
        return self.sound.upper()

#Goblin subclass of Monster or it extends monster.

class Goblin(Monster):
    max_hit_pts = 3
    max_experience = 2
        pass
