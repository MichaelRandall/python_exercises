#!/usr/bin/env python

my_list=[1,2,"a","b","c","d",5,6,7,"f","g","h",8,9,"j"]
print my_list

my_list[:2]
print my_list

del my_list[:2] # removes 1 and 2


#replace 5,6,7 with the letter e and f
my_list[4:7] = ["e","f"]

my_list.remove("f") #gets rid of the extra f


my_list[8:10] = ["i"] #I could just use "i" without list notation to replace
print my_list


my_list[0:2] = ["z","z","z","z","z"] #replaces a and b with 5 zs
print my_list

my_list[0:2] = ["k"]*5 #replaces 2 zs with 5 ks
print my_list


def sillycase(input_string):
    operation_string = list(input_string)
    first = len(operation_string)/2
    print type(first)
    first_part_string = operation_string[:first]
    last_part_string = operation_string[first:]

    for item in first_part_string:
        f_item_idx = first_part_string.index(item)
        print type(f_item_idx)
        first_part_string[f_item_idx] = item.lower()

    for item in last_part_string:
        l_item_idx = last_part_string.index(item)
        print type(l_item_idx)
        last_part_string[l_item_idx] = item.upper()
    input_string = ' '.join(first_part_string + last_part_string)
    print type(input_string)
    return input_string
    

print sillycase("Treehouse")
