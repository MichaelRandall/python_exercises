#!/usr/bin/env python

def add_list(a_list):
  counter = 0
  for a in a_list:
    counter = counter + int(a)
  return counter

def summarize(b_list):
  theList = " ".join(str(b_list))
  
  counter_x = 0
  
  for b in b_list:
    counter_x = counter_x + int(b)
  
  return "The sum of {} is {}.".format(theList, counter_x)

print summarize([1,2,3])
