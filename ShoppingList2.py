#!/usr/bin/env python


shopping_list = []

def show_help():
    print("\nSeparate each item with a comma.")
    print("Type DONE to quit, SHOW to see the current list, and HELP to get this message.")

def show_list():
    count = 1
    for item in shopping_list:
        print("{}: {}".format(count,item))
        count += 1

print("Give me a list of things you want.")
show_help()

while True:
    new_stuff = raw_input("> ")

    if new_stuff == "DONE":
        print("\nHere's your list")
        show_list()
        break
    elif new_stuff == "HELP":
        show_help()
        continue
    elif new_stuff == "SHOW":
        show_list()
        continue
    else:
        new_list = new_stuff.split(",")
        index = raw_input("Add this at a certain spot? Press 'Enter' for the end of the list, "
                          "or give me a number. Currently {} items in the list. ".format(
                          len(shopping_list)))
        if index:
            spot = int(index) - 1
            for item in new_list:
                shopping_list.insert(spot, item.strip())
                spot += 1
        else:
            for item in new_list:
                shopping_list.append(item.strip())
    

print("What should we buy?")
print("Enter 'DONE' to stop adding items")


while True:
    new_item = raw_input("> ")

    if new_item == "DONE":
        break

    shopping_list.append(new_item)
    print("Added! Your list has {} items.".format(len(shopping_list)))
    continue

print("Here's your list:")

for item in shopping_list:
    print item


print ", ".join(shopping_list)
