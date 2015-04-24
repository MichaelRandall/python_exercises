#!/usr/bin/env python

#my function learning

def return_greeting():
    print("Hello!")


def add_to_four(num):
    print(num + 4)

def get_word(phrase):
    my_wordz_list = phrase.split()
    print("my_wordz_list has {} items.".format(len(my_wordz_list)))
    
def square(num):
    return num * num


return_greeting()

add_to_four(6)

print("Enter a phrase!")

my_phrase = raw_input("Start writing: ")

get_word(my_phrase)

print square(5)

