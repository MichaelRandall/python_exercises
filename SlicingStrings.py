#!/usr/bin/env python


my_string = "Hello there"

print my_string[1:5]  #returns ello

print my_string[2]



my_list = list(range(1,6))
print my_list
print my_list[1:3]

print my_list[1:len(my_list)]

# the list has 5 items we need to use 4
# leave off the first number, we start at 0
# leave off the last number, we go to the end
# [:] returns all of my list

my_new_list = [4,2,3,1,5]
my_sorted_list = my_new_list[:] #way to copy a list so you can keep the original

print my_new_list
print my_sorted_list

print sorted(my_sorted_list) #returns my_sorted_list, but sorted


new_list = list(range(20)) # creates a list with a range from 0 - 19
print new_list
print new_list[::2] # go from beginning to end and add two at each time
print new_list[2::2] # starts at index 2 and moves two at a time

print "Nebraska"[::-1] # reverses the string by starting at the back instead of the front
print new_list[::-1]
print new_list[::-2] # returns the list backwards moving two at a time

print new_list[2:8:-1] # wont work because we start at 2 and count backwards
print new_list[8:2:-1] # says start at 8 and work your way back one at a time until reach two

print new_list[7-1] # starts at 7 and works down to 2
