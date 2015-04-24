#!/usr/bin/env python

the_list=["a",2,3,1,False,[1,2,3]]

#Challenge is to move the first instance of 1 to the 0 index position

the_list.insert(0, the_list.pop(3))

#print the_list
#del the_list[5]
#print the_list

#Challenge use remove and/or delete to remove the string, boolean, and list members
removeable_items = []
for item in the_list:
    if type(item) != int:
        del_item_idx = the_list.index(item)
        removeable_items.append(del_item_idx)
        
rev_rem_items = removeable_items[::-1]
for item in rev_rem_items:
    del the_list[item]
    
the_list.extend(range(4,21))

print the_list
#print type(the_list[3])
