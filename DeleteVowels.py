#!/usr/bin/env python

def delete_vowels(a_string):
    vowels = list("aeiou")
    parsed_sen = a_string.split()

    output = []

    for word in parsed_sen:
        word_list = list(word.lower())

        for vowel in vowels:
            while True:
                try:
                    word_list.remove(vowel)
                except:
                    break
        output.append(" ".join(word_list).capitalize())
    print(output)
    



print("\nWrite a sentence. ")

my_string = raw_input("> ")

delete_vowels(my_string)
 
