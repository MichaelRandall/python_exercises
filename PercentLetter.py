#!/usr/bin/env python

user_string = raw_input("What your word? ")
user_count = raw_input("Whats your number? ")

try:
    our_num = int(user_count)
except:
    our_num = float(user_count)


if not "." in user_count:
    print(user_string[our_num])
else:
    ratio = round(len(user_string)*our_num)
    #print ratio
    print(user_string[ratio])
