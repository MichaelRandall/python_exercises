#!/usr/bin/env python

my_num_list = [1,3,5,7,9,11,13,15.5]
my_str_list = ["I","like","pizza"]
my_mix_list = ["cabbage",4,"bunnies",6,"termites",2,"cars",3.6]

hello_list = 3

if hello_list in my_num_list:
    print str(hello_list) + " is in my_num_list"
else:
    print "not found"


my_phrase = "Peanut butter and marshmallows are really good"
my_word = "Auspicious"
my_sent_list = my_phrase.split()


print "The item at index 0 is " + my_mix_list[0]
print my_mix_list
print "The length of my_mix_list is " + str(len(my_mix_list))
print "my_word listed looks like this " + str(list(my_word))
print "my_phrase split looks like this " + str(my_phrase.split())

print "I will now rejoin my_phrase."
print "^+^".join(my_sent_list)
print "One more time"
print " ".join(my_sent_list)

print ' + '.join([1,2,3])


