#!/usr/bin/env python

#Collections are variable types that collect bits of data together aka interables
#strings and lists

aList = [1,2,3]
aList.append([4,5]) #returns[1,2,3[4,5]]

print aList

# range method
our_list= list(range(10)) #returns 0-9
print our_list

print our_list + [10,11,12] #returns 0-12

print our_list #why does this show our_list as 0-9 after adding the other list???

our_list = our_list + [10,11,12]
print our_list


list_1 = ["Dogs","Cats","Snakes"]
list_2 = ["Ferrets","Mice","Rats"]
list_3 = list_1 + list_2
print list_3

# .extend()
# .insert()


our_list.extend(range(13,21)) #returns the updated list between 0 and 20
print our_list


alpha = list("acdf") #notice that alpha takes a string but returns a list
print alpha

alpha.insert(1, 'b')
print alpha
alpha.insert(4, 'e')
print alpha
