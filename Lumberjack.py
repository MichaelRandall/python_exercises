#!/usr/bin/env python

name = raw_input("What's your name? ")
job = "cook"

if name == "Michael":
    print(name + " is learning stuff.")
else:
    print("{} is not recognized as learning stuff to {}.".format(name,job))
