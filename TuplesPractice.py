#!/usr/bin/env python

#tuples are immutable - can't be changed

my_tuple = (1, 2, 3)

print my_tuple

my_tuple_2 = 1, 2, 3

print my_tuple_2

#both above are the same - the first is easier to read and understand


my_tuple_3 = tuple([1,2,3])
print my_tuple_3

print my_tuple[1]

#my_tuple[0] = 4 generates an error since tuples are immutable
print my_tuple[0]

#packing and unpacking with tuples
#set multiple variables at once

a, b = 1, 2
print a
print b

#==============================================================================

#we are creating two tuples with 3 variables and assigning values in one tuple
#to the other tuple's variables - called simultaneous assignment
#the first tuple contains name, age, phone, the second tuple contains the other

name, age, phone = "Mike", 47, 3608236316

print name
print age


print phone

#unpacking a tuple
c = (3, 4)
#c = 3,4 would also work
d,e = c
print "Example of unpacking tuples"
print "c is a tuple consisting of " + str(c)
print 'd is a variable that hold the first value of c: ' +  str(d)
print 'e is a variable that hold the second value of c: ' + str(e)

#packing a tuple
f = d,e
print "Example of packing"
print "f is assigned both d and e (f = d,e) so it now is packed with: " + str(f)

print f == c

#deleting tuple items
del a
del b

a = 1
b = 2

#swap variables
a, b = b, a

print a
print b


def my_func():
    return 1, 2, 3

print my_func()

tup = my_func() # returns a tuple of 1, 2, 3

x,y,z = my_func() # returns 1 for x, 2 for y, 3 for z

print x
print y
print z


#challenge - take a string and return it as a tuple with upper, lower, title, and reverse
def stringcases(a_str):
    tup = a_str.upper(), a_str.lower(), a_str.title(), a_str[::-1]
    return tup

print stringcases("I like peanut butter")



#tuples with functions
my_alpha_bits = list("abcdefghijklmnopqrstuvwxyz")
print my_alpha_bits

#The next 4 all yeild the same results - iterate over a list of items displaying num and val

#count = 0
#for letter in my_alpha_bits:
#    print('{}: {}'.format(count, letter))
#    count += 1


#for index, letter in enumerate(my_alpha_bits):
#    print('{}: {}'.format(index, letter))


#for step in enumerate(my_alpha_bits):
#    print('{}: {}'.format(step[0], step[1]))


#single stars take apart tuples and lists, two stars take apart dictionaries

for step in enumerate(my_alpha_bits):
    print('{}: {}'.format(*step))


#go through and get keys and values in dict using items instead of enumerate
my_dict10 = {"name":"Michael","job":"Writer","employer":"Self-Employed"}
for key, value in my_dict10.items():
    print('{}: {}'.format(key.title(), value))


#code challenge - take two iterables, with the same number of elements
#return a list containing tuples of each item in each list [{1,1},{2,2}]
def combo(a_it, b_it):
    tup_list = []
    for a, b in zip(a_it, b_it):
        tup_holder = a, b
        tup_list.append(tup_holder)
    return tup_list

a_it = ["one","two","three"]
b_it = ["a","b","c"]

print combo(a_it, b_it)







