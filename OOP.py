#! /usr/bin/python

#classes start with caps

class Monster(object):
    hit_points = 1
    name = 'Bob'
    color = 'green'
    weapon = 'spear'
    

#create an instance of Monster
Harold_Monster = Monster()
print(type(Harold_Monster))
print(Harold_Monster.weapon)
#print Monster.color
#print Monster.weapon

mike = Monster()
mike.name = "Mike"
mike.weapon = "horrific features"

print mike.weapon

