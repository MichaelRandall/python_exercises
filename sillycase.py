#!/usr/bin/env python




def sillycase(a_string):
    first = int(round(len(a_string)/2))
    print first
    print type(first)
    return ''.join(a_string[:first].lower() + a_string[first:].upper())
  
    #input_string = ''.join(first_part_string + last_part_string)
    #print type(input_string)
    #return input_string
    

print sillycase("Treehouse")
