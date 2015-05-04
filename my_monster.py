#! /usr/bin/python

from monster import Monster

scary = Monster()

scary.name = 'Bob'
scary.weapon = 'torch'
scary.color = 'black'


print scary.weapon
print scary.battlecry()

scary.sound = "Moo"

print scary.battlecry()
print scary.warning()
