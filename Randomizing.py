#! /usr/bin/python
import random

my_list = list(range(26))

print my_list

print random.choice(my_list)

print random.choice([(0,1), (2,3), (4,5), (6,7),(8,9)])


my_int = 4
my_iter = list(range(10))

def nchoices(my_iter, my_int):
    ran_list = []
    i = 0
    while i < my_int:
        ran_list.append(random.choice(my_iter))
        i += 1
    return ran_list

print nchoices(my_iter, my_int)
