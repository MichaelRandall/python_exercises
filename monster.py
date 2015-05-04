#! /usr/bin/python

class Monster(object):
    hit_points = 1
    name = "Jerome"
    color = "orange"
    weapon = "horrific features"
    sound = "squeak"
    message = "Look out because I'm {}".format(color)

    def battlecry(self):
        return self.sound.upper()

    def warning(self):
        return self.message
