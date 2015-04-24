#!/usr/bin/env python

a_list = list("abczdef")

print a_list #returns the list of items
print a_list.index('z') # returns the index for z

del a_list[3] #deletes the item at index 3 which is z
print a_list

a_string = "Eat some pizza!"
print a_string
del a_string
#print a_string - generates an error because we deleted this

a_num = 6
print a_num
del a_num
#print a_num - generates an error because we deleted this

a_string2 = "Waacky"
#del a_string2[1] - this won't work because strngs are immutable and don't support delete item 
