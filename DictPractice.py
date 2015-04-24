#!/usr/bin/env python

#dictionaries don't have an order so we can't use indexes

my_dict = {'name': "Michael"}

my_dict['name']

my_dict = {"name": "Michael", "job": "Writer"}

print my_dict

#values can be lists, strings, booleans, or other dictionaries, or objects, or custom classes

name_dict = {"names": {'first': "Michael", 'last': "Randall"}}

#keys can be strings, numbers, tuples, boolean

game_dict = {(2, 2): True, (1, 2): False}

#delete keys, change their values, or add batches to a dictionary



def members(a_dict, a_list):
  item_count = 0
  for item in a_list:
    if item in a_dict.keys():
      item_count += 1
  return item_count

a_list = ["tomatoes","onions","cheese","lettuce"]

a_dict = {"tomatoes":1, "french fries":2, "hamburger":3}

print members(a_dict, a_list)
#----------------------------------------------------------
#deleting keys
my_emp_dict = {"name": "Michael", "job": "Writer"}
del my_emp_dict['job'] #removes the job key and value
print my_emp_dict

#----------------------------------------------------------
#adding keys and values
my_emp_dict['age'] = 45

#----------------------------------------------------------
#changing value for a key
my_emp_dict['age'] = 46
print my_emp_dict

#----------------------------------------------------------
#adding multiple keys and values
my_emp_dict.update({'job':'writer', 'age':47, 'state': 'Oregon', 'name': 'Michael Randall'})
print my_emp_dict



def word_count(a_str):
    a_str_1 = (a_str[:].lower()).split()
    a_str_2 = (a_str[:].lower()).split()
    my_dict = {}
    for word in a_str_1:
        if word in my_dict.keys():
            my_dict[word] += 1
        else:
            my_dict[word] = 1
        
    print a_str_1
    print my_dict

word_count("I like peanut butter with jelly and peanut butter with honey.")


#unpacking dictionaries
my_str = "Hi! my name is {name} and I live in {state}."

my_str.format(name = "Mike", state= 'Oregon')

print my_str.format(name = "Mike", state = "Oregon")

my_dict_3 = {"name":"Mike","state":"Oregon"}

print my_str.format(**my_dict_3)

#challenge
dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasagna'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
    ]

string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(a_list_dicts, a_str):
    full_list = []
    for item in a_list_dicts:
        full_list.append(a_str.format(**item))
    return full_list

print string_factory(dicts, string)


#iterating dicts
my_dict_4 = {'name': "Michael", 'age': '46', 'state': 'Oregon', 'country': 'USA', 'employer': 'eBay', 'job': 'writer'}
print my_dict_4

for item in my_dict_4:
    print item #returns keys

#above and below return the same, keys

for key in my_dict_4.keys():
    print key #returns keys


for key in my_dict_4.keys():
    print my_dict_4[key] #returns values

#above and below return the same, values

for value in my_dict_4.values():
    print value # returns the values


for key in my_dict_4.keys():
    print key + ": " + my_dict_4[key] #returns keys and their values


#challenge

def most_classes(a_dict):
  max_count = 0
  max_count_holder = ""
  
  for key in a_dict.keys():
    print len(a_dict[key])
    if len(a_dict[key]) > max_count:
      max_count = len(a_dict[key])
      max_count_holder = key

  return max_count_holder


a_dict = {"bob":["one", "two", "three"], "mike":["one","two"]}

print most_classes(a_dict)


def num_teachers(a_dict):
  teacher_count = 0
  for key in a_dict:
    teacher_count += 1

  return teacher_count

print num_teachers(a_dict)


def stats(a_dict):
  stats_list = []

  for item in a_dict:
    new_list = []
    new_list.append(item)
    new_list.append(len(a_dict[item]))
    stats_list.append(new_list)
  return stats_list

print stats(a_dict)


def courses(b_dict):
  course_list = []
  for name in b_dict:
    for item in b_dict[name]:
      course_list.append(item)
  return course_list


b_dict = {"Mike":["course 1", "course 2", "course 3", "course 4"],
          "Bob":["course 2", "course 3", "course 4"],
          "Rocky":["course 4", "course 5", "course 6"]}

print courses(b_dict)
        




