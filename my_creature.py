#! /usr/bin/python

from dunder_init import Creature, Auto, Animal

ducky = Creature(20, "smell", "green", "hiccup")

print(ducky)
print(ducky.color)
print(ducky.battlecry())


my_car = Auto()
print(my_car.make)

his_car = Auto(door_cnt=2)
print(his_car.make)
print(his_car.door_cnt)


my_animal = Animal(size="large", sound="pawooh")

print(my_animal.attackcry())

del my_animal


print(my_animal.size)
