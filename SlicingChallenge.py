#!/usr/bin/env python
def first_4(my_iter):
    return my_iter[:4]

def odds(my_iter):
    return my_iter[1::2]

def first_and_last_4(my_iter):
    my_first_iter = my_iter[:]
    my_last_iter = my_iter[:]

    my_first_last = my_first_iter[:4] + my_last_iter[len(my_last_iter)-4:len(my_last_iter):1]
    return my_first_last
    #should return the first four and last four of a list passed to it

print first_4([2,4,6,8,10,12,14,16,18,20])
print odds([2,4,6,8,10,12,14,16,18,20])
print first_and_last_4([2,4,6,8,10,12,14,16,18,20])
